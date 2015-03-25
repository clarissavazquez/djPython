from __future__ import division
import wave
import struct
import numpy
from numpy import argmax, sqrt, mean, diff, log
from scipy import signal
from matplotlib.mlab import find
from time import time
import sys
import os
from abjad import *
from array import array

if len(sys.argv) == 1: # Checks for correct input from the command line
	print "Must include a wave filename"
	print "USAGE: 'python extracts_info.py FILENAME.wav'"
	print
	exit()
else: # Allows arguments to pass through into the program if good input
	FILENAMES = []
	for files in sys.argv[1:]: 
		FILENAMES.append(files)
	
#	FILENAME = sys.argv[1]
#DATASIZE = os.path.getsize(FILENAME)
FRAMERATE = 44100




def open_file(FILENAME):
	print "===========================================";
	# Summary: Opens a wav file to extract all the properties of the 
	# sound wav file. We will later use the information/properties 
	# that were extracted to calculate the frequencies.
	wav = wave.open(FILENAME, 'r') # opens and reads the wav file

	(nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams() 
	# Extracts the desired properties/information

	frames = wav.readframes(nframes * nchannels) 
	# Calculates the frame rate
	# Frame rate is the frequency at which frames of the sound 
	# are played

	out = struct.unpack_from ("%dh" % nframes * nchannels, frames)
	# Goes through the array of the sound and extracts the desired
	# and necessary properties that are used for calculations for 
	# the frequency
	print "Filename:", FILENAME			# Displays properties of the file
	print "Channels:", nchannels			# to test for correctness. 
	print "SampleWidth:", sampwidth
	print "Framerate:", framerate
	print "Number of Frames:", nframes
	return out

def fftConvert(frames, fs):
	# Summary: Extracts variables necessary to calculate the frequency
	# Makes calculation more accurate by getting rid of any negative values
	autocorrelated = signal.fftconvolve(frames, frames[::-1], mode = 'full')
	autocorrelated = autocorrelated[len(autocorrelated) / 2:]

	# Finds the first low value to calculate
	difference = diff(autocorrelated)
	start = find(difference > 0)[0]
	
	# Finds the next peak to calculate with, ignoring any 0s
	peak = argmax(autocorrelated[start:]) + start
	px, py = parabolic(autocorrelated, peak)
	return fs / px

def parabolic(f, x):
	# Summary: This is a parabolic equation that finds the peak of the wave and returns
	# the coordinates of that point. This point is significant because it
	# represents the main frequency.
	xv = 1/2 * (f[x-1] - f[x+1]) / (f[x-1] - 2 * f[x] + f[x+1]) + x
	yv = f[x] - 1/4 * (f[x-1] - f[x+1]) * (xv - x)
	return (xv, yv)

def extractNotes(frequencies):
	# Summary: Passes the calculated frequencies in so it can be called into the 
	# translateNote function. This function mainly serves to retrieve and pass the
	# information/properties of the sound files. 
	variable = []  # Empty array declared which will be filled with the notes.  
	for i in frequencies:
		# Iterates through the frequencies and passes them into the function
		# which translates the notes from frequencies to actual notes. 
		tones = translateNote(i)
		variable.append(tones)  # Adds the notes to the variable array. 

        pitch_numbers = variable		# Gets the array and pitch
        duration = Duration(1,4)    # Assigns the duration of the note
        note = scoretools.make_notes(pitch_numbers, duration)  # Creates the score	
        
        staff= Staff(note)  # Creates the staff, sets the notes to the
        show(staff) 			# corresponding spot and then displays staff

def translateNote(frequency):
		# Summary: Takes in frequencies and runs through this if statement
		# to find its corresponding note indicator. Returns the note to be
		# passed into the function where the note is displayed. 
	if frequency >= 16.352 and frequency <= 17.324:
                note = -48 # C0
        elif frequency >= 18.354 and frequency <= 19.445:
                note = -46 # D0
        elif frequency >= 20.602 and frequency < 21.827:
                note = -44 # E0
        elif frequency >= 21.827 and frequency <= 23.125:
                note = -43 # F0
        elif frequency >= 24.500 and frequency <= 25.957:
                note = -41 # G0
        elif frequency >= 27.5  and frequency <= 29.135:
                note = -39 #A0
        elif frequency >= 30.868 and frequency < 32.703:
                note = -37 #B0
        elif frequency >= 32.703 and frequency <= 34.648:
                note = -36 #C1
        elif frequency >= 36.708 and frequency <= 38.891:
                note = -34 #D1
        elif frequency >= 41.1 and frequency < 43.654:
                note = -32  #E1
        elif frequency >= 43.654 and frequency <= 46.249:
                note = -31 #F1
        elif frequency >= 48.999 and frequency <= 51.9:
                note = -29 #G1
        elif frequency >= 54.3 and frequency <= 58.270:
                note = -27 #A1
        elif frequency >= 61.735 and frequency < 65.406:
                note = -25 #B1
        elif frequency >= 65.406 and frequency <= 69.296:
                note = -24 #C2
        elif frequency >= 72.716 and frequency <= 77.782:
                note = -22 #D2
        elif frequency >= 81.707 and frequency < 87.307:
                note = -20 #E2
        elif frequency >= 87.307 and frequency <= 92.499:
                note = -19 #F2
        elif frequency >= 97.299 and frequency <= 103.83:
                note = -17 #G2
        elif frequency >= 109.3 and frequency <= 116.57:
                note = -15 #A2
        elif frequency >= 122.77 and frequency < 130.81:
                note = -13 #B2
        elif frequency >= 130.11 and frequency <= 138.59:
                note = -12 #C3
        elif frequency >= 146.13 and frequency <= 155.56:
                note = -10  #D3
        elif frequency >= 164.11 and frequency <= 174.61:
               note = -8 #E3
        elif frequency >= 173.91 and frequency <= 185.31:
                note = -7 #F3
        elif frequency >= 195.3 and frequency <= 207.65:
                note = -5 #G3
        elif frequency >= 219.3 and frequency <= 233.08:
                note = -3 #A3
	elif frequency >= 246.94 and frequency < 261.63:
                note = -1 #B3
        elif frequency >= 260.93 and frequency <= 277.33:
                note = 0 #C'4
        elif frequency >= 292.97 and frequency <= 311.37:
                note = 2 #D'4
        elif frequency >= 328.63 and frequency < 349.23:
                note = 4 #E'4
        elif frequency >= 348.53 and frequency <= 369.93:
                note = 5 #F'4
        elif frequency >= 391.3 and frequency <= 415.7:
                note = 7 #G'4
        elif frequency >= 439.3 and frequency <= 466.7:
                note = 9 #A'4
        elif frequency >= 493.18 and frequency <= 523.58:
                note = 11 #B4
        elif frequency >= 522.8 and frequency <= 554.2:
                note = 12 #C'5
        elif frequency >= 586.63 and frequency <= 622.23:
                note = 14 #D'5
        elif frequency >= 658.56 and frequency < 698.46:
                note = 16 #E'5
        elif frequency >= 698.46 and frequency <= 739.96:
                note = 17 #F'5
        elif frequency >= 783.29 and frequency <= 830.69:
                note = 19 #G'5
        elif frequency >= 879.3 and frequency <= 932.33:
                note = 21 #A'5
        elif frequency >= 987.07 and frequency < 1046.5:
                note = 23 #B'5
        elif frequency >= 1046.5 and frequency <= 1108.7:
                note = 24 #C'6
        elif frequency >= 1174.7 and frequency <= 1244.5:
                note = 26 #D6
        elif frequency >= 1318.5 and frequency < 1396.9:
                note = 28 #E6
        elif frequency >= 1396.9 and frequency <= 1480.0:
                note = 29 #F6
        elif frequency >= 1568.0 and frequency <= 1661.2:
                note = 31 #G6
	elif frequency >= 1760.0 and frequency <= 1864.7:
                note = 33 #A6
        elif frequency >= 1975.5 and frequency < 2093.0:
                note = 35 #B6
        elif frequency >= 2093.7 and frequency <= 2217.5:
                note = 36 #C7
        elif frequency >= 2349.3 and frequency <= 2489.0:
                note = 38 #D7
        elif frequency >= 2637.0 and frequency < 2793.8:
                note = 40 #E7
        elif frequency >= 2793.8 and frequency <= 2960.0:
                note = 41 #F7
        elif frequency >= 3136.0 and frequency <= 3322.4:
                note = 43 #G7
        elif frequency >= 3520.0 and frequency <= 3729.3:
                note = 45 #A7
        elif frequency >= 3951.1 and frequency < 4186.0:
                note = 47 #B7
        elif frequency >= 4186.0 and frequency <= 4434.9:
                        note = 48 #C8
        elif frequency >= 4698.6 and frequency <= 4978.0:
                        note = 50 #D8
        elif frequency >= 5274.0 and frequency < 5587.7:
                        note = 52 #E8
        elif frequency >= 5587.7 and frequency <= 5919.9:
                        note = 53 #F8
        elif frequency >= 6271.9 and frequency <= 6644.9:
                        note = 55 #G8
        elif frequency >= 7040.0 and frequency <= 7458.6:
                        note = 57 #A8
        elif frequency >= 7902.1 and frequency <= 8372.0:
                        note = 59 #B8
        elif frequency >= 8372.0 and frequency <= 8869.8:
                        note = 60 #C9
        elif frequency >= 9397.3 and frequency <= 9956.1:
                        note = 62 # D9
        elif frequency >= 10548.1 and frequency < 11175.3:
                        note = 64 #E9
        elif frequency >= 11175.3 and frequency <= 11839.8:
                        note = 65 #F9
   	elif frequency >= 12543.9 and frequency <= 13289.8:
                        note = 67 #G9
        elif frequency >= 14080.0 and frequency <= 14917.2:
                        note = 69 #A9
        elif frequency >= 15804.3 and frequency < 16744.0:
                        note = 71 #B9
        elif frequency >= 16744.0 and frequency <= 17739.7:
                        note = 72 # C10
        elif frequency >= 18794.5 and frequency <= 19912.1:
                        note = 74 #D10
        elif frequency >= 21096.2 and frequency < 22350.6:
                        note = 76 #E10
        elif frequency >= 22350.6 and frequency <= 23679.6:
                        note = 77 #F10
        elif frequency >= 25087.7 and frequency <= 26579.5:
                        note = 79 #G10
        elif frequency >= 28160.0 and frequency <= 29834.5:
                        note = 81 #A10
        elif frequency >= 31608.5:
                        note = 83 #B10
        else:
                print "Incorrect Input"
        return note



def main():
	frequencies = []  # Declares an empty array where we will store frequencies
	for FILENAME in FILENAMES:
		frames = open_file(FILENAME)  # Extracts the sound properties
		autocorrelated = fftConvert(frames, 44100)  # Calculates frequencies
		frequencies.append(autocorrelated)  # Adds the frequencies into the array
	#print 'Calculating frequency from autocorrelation:',
	#start_time = time()
	#print '%f Hz' % autocorrelated(signal, fs)
	#print 'Time elapsed: %.3f s\n' % (time() - start_time)
	
#		writenotes = open('testFrequencies.txt', 're')
	#	writenotes.write(str(autocorrelated))
	#	writenotes.write('\n')
	#	writenotes.close()
		print "Frequency: " , autocorrelated
		print
	extractNotes(frequencies)  # Passes frequencies into function where notes are displayed
	
#		print "Found Frequency:", autocorrelated
#	os.remove('musicFrequencies.txt')

main()














