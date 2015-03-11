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
from clarissa import readNotes

if len(sys.argv) == 1:
	print "Must include a wave filename"
	print "USAGE: 'python extracts_info.py FILENAME.wav'"
	print
	exit()
else:
	FILENAMES = []
	for files in sys.argv[1:]: 
		FILENAMES.append(files)
		print files

#	FILENAME = sys.argv[1]
#DATASIZE = os.path.getsize(FILENAME)
FRAMERATE = 44100




def open_file(FILENAME):
	wav = wave.open(FILENAME, 'r') # opens and reads the wav file

	(nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams() # Gets the appropriate 											 #things

	frames = wav.readframes(nframes * nchannels) # calcs the framerate

	out = struct.unpack_from ("%dh" % nframes * nchannels, frames)
	
	left = out[0:2] # we will only be dealing with one channel
			# dual channel is not nessesary since we are only
			# reading notes
	print "Filename:", FILENAME
	print "Channels:", nchannels
	print "SampleWidth:", sampwidth
	print "Framerate:", framerate
	print "Number of Frames:", nframes
	return out

def fftConvert(frames, fs):
	
	# This makes our calc more accurate by getting rid of any negative values
	autocorrelated = signal.fftconvolve(frames, frames[::-1], mode = 'full')
	autocorrelated = autocorrelated[len(autocorrelated) / 2:]

	# Now to find the first low value to calculate
	difference = diff(autocorrelated)
	start = find(difference > 0)[0]
	
	# Now to find the next peak to calculate with, ignoring any 0s
	peak = argmax(autocorrelated[start:]) + start
	px, py = parabolic(autocorrelated, peak)
	return fs / px

def parabolic(f, x):

	# This is a parabolic equation that finds the peak of the wave and returns the coordinates of that point
	# This point is significatnt to us because it represents the main frequency

	xv = 1/2 * (f[x-1] - f[x+1]) / (f[x-1] - 2 * f[x] + f[x+1]) + x
	yv = f[x] - 1/4 * (f[x-1] - f[x+1]) * (xv - x)
	return (xv, yv)
	

def main():
	
	for FILENAME in FILENAMES:

		frames = open_file(FILENAME)
		autocorrelated = fftConvert(frames, 44100)

	#print 'Calculating frequency from autocorrelation:',
	#start_time = time()
	#print '%f Hz' % autocorrelated(signal, fs)
	#print 'Time elapsed: %.3f s\n' % (time() - start_time)
	
		writenotes = open('musicFrequencies.txt', 'a')
		writenotes.write(str(autocorrelated))
		writenotes.write('\n')
		writenotes.close()
		readNotes()

		print "Found Frequency:", autocorrelated
	os.remove('musicFrequencies.txt')

main()














