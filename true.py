import wave
import struct
import numpy
from scipy import signal


def open_file():
	wav = wave.open("test2.wav", 'r') # opens and reads the wav file

	(nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams() # Gets the appropriate 											 #things

	frames = wav.readframes(nframes * nchannels) # calcs the framerate

	out = struct.unpack_from ("%dh" % nframes * nchannels, frames)
	
	left = out[0:2] # we will only be dealing with one channel
			# dual channel is not nessesary since we are only
			# reading notes
	print nchannels
	print sampwidth
	print framerate
	print nframes

def feq():
	# 1/2.0 * (signal[peak - 1] - signal[peak + 1]) / (signal[peak - 1] -2 *signal[peak] + signal[peak + 1]) + peak
	fftconvolve()

def main():
	open_file()

main()
