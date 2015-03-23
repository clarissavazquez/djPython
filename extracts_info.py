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
        if frequency > 25.957 and frequency < 29.135:
                note = -40 #A0
        elif frequency >= 29.135 and frequency < 31.568:
                note = -38 #B0
        elif frequency >= 32.003 and frequency <= 33.403:
                note = -37 #C1
        elif frequency >= 29.708 and frequency <= 31.108:
                note = -36 #D1
        elif frequency >= 40.503 and frequency <= 41.903:
                note = -34  #E1
        elif frequency >= 42.954 and frequency <= 44.354:
                note = -32 #F1
        elif frequency >= 48.299 and frequency <= 51.9:
                note = -29 #G1
        elif frequency >= 54.3 and frequency <= 55.7:
                note = -27 #A1
        elif frequency >= 61.035 and frequency <= 62.435:
                note = -25 #B1
        elif frequency >= 64.706 and frequency <= 66.106:
                note = -24 #C2
        elif frequency >= 72.716 and frequency <= 74.116:
                note = -22 #D2
        elif frequency >= 81.707 and frequency <= 83.107:
                note = -20 #E2
        elif frequency >= 86.607 and frequency <= 88.007:
                note = -19 #F2
        elif frequency >= 97.299 and frequency <= 98.669:
                note = -17 #G2
        elif frequency >= 109.3 and frequency <= 110.7:
                note = -15 #A2
        elif frequency >= 122.77 and frequency <= 124.17:
                note = -13 #B2
        elif frequency >= 130.11 and frequency <= 131.51:
                note = -12 #C3
        elif frequency >= 146.13 and frequency <= 147.53:
                note = -10  #D3
        elif frequency >= 164.11 and frequency <= 165.51:
               note = -8 #E3
        elif frequency >= 173.91 and frequency <= 175.31:
                note = -7 #F3
        elif frequency >= 195.3 and frequency <= 196.7:
                note = -5 #G3
        elif frequency >= 219.3 and frequency <= 220.7:
                note = -3 #A3
        elif frequency >= 246.24 and frequency <= 247.64:
                note = -1 #B3
        elif frequency >= 260.93 and frequency <= 262.33:
                note = 0 #C'4
        elif frequency >= 292.97 and frequency <= 294.37:
                note = 2 #D'4
        elif frequency >= 328.93 and frequency <= 330.33:
                note = 4 #E'4
        elif frequency >= 348.53 and frequency <= 349.93:
                note = 5 #F'4
        elif frequency >= 391.3 and frequency <= 392.7:
                note = 7 #G'4
        elif frequency >= 439.3 and frequency <= 440.7:
                note = 9 #A'4
        elif frequency >= 493.18 and frequency <= 494.58:
                note = 11 #B4
        elif frequency >= 522.8 and frequency <= 524.2:
                note = 12 #C'5
        elif frequency >= 586.63 and frequency <= 588.03:
                note = 14 #D'5
        elif frequency >= 658.56 and frequency <= 659.96:
                note = 16 #E'5
        elif frequency >= 697.76 and frequency <= 699.16:
                note = 17 #F'5
        elif frequency >= 783.29 and frequency <= 784.69:
                note = 19 #G'5
        elif frequency >= 879.3 and frequency <= 880.7:
                note = 21 #A'5
        elif frequency >= 987.07 and frequency <= 988.47:
                note = 23 #B'5
        elif frequency >= 1045.8 and frequency <= 1047.2:
                note = 24 #C'6
        elif frequency >= 1174 and frequency <= 1175.4:
                note = 26 #D6
        elif frequency >= 1317.8 and frequency <= 1319.2:
                note = 28 #E6
        elif frequency >= 1396.2 and frequency <= 1397.6:
                note = 29 #F6
        elif frequency >= 1567.3 and frequency <= 1568.7:
                note = 31 #G6
        elif frequency >= 1759.3 and frequency <= 1760.7:
                note = 33 #A6
        elif frequency >= 1974.8 and frequency <= 1976.2:
                note = 35 #B6
        elif frequency >= 2092.3 and frequency <= 2093.7:
                note = 36 #C7
        elif frequency >= 2348.6 and frequency <= 2350:
                note = 38 #D7
        elif frequency >= 2636.3 and frequency <= 2637.7:
                note = 40 #E7
        elif frequency >= 2792.3 and frequency <= 2793.7:
                note = 41 #F7
        elif frequency >= 3135.3 and frequency <= 3136.7:
                note = 43 #G7
        elif frequency >= 3519.3 and frequency <= 3520.7:
                note = 45 #A7
        elif frequency >= 3950.4 and frequency <= 3951.8:
                note = 47 #B7
        elif frequency == 4186.0:
                note = 48 #C8
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














