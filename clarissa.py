from abjad import *
from array import array
import fileinput

def readNotes():
	f = open('musicFrequencies.txt', 'r')
	frequencies =[float(n) for n in f.read().split()]

	variable = []	#array that will take the notes as integers
	for i in frequencies:
		tones = Note(translateNotes(i))	# will translate frequencies
		variable.append(tones)	#adds the integers to the array
	
	pitch_numbers = variable	#gits the array and get pitch
	duration = Duration(1,4)	#states the duration of the notes
	note = scoretools.make_notes(pitch_numbers, duration)	#converts integers to notes
	staff= Staff(note)	#creates a staff and sets the notes on them
	show(staff)	#shows the staff
	
def translateNotes(frequency):
	if frequency >= 26.8 and frequency <= 28.2:
		note = "a'0"
	elif frequency >= 30.168 and frequency <= 31.568:
		note = "b'0"
	elif frequency >= 32.003 and frequency <= 33.403:
		note = "c'1"
	elif frequency >= 29.708 and frequency <= 31.108:
		note = "d'1"
	elif frequency >= 40.503 and frequency <= 41.903:
		note = "e'1"
	elif frequency >= 42.954 and frequency <= 44.354:
		note = "f'1"
	elif frequency >= 48.299 and frequency <= 49.699:
		note = "g'1"
	elif frequency >= 54.3 and frequency <= 55.7:
		note = "a'1"
	elif frequency >= 61.035 and frequency <= 62.435:
		note = "b'1"
	elif frequency >= 64.706 and frequency <= 66.106:
		note = "c'2"
	elif frequency >= 72.716 and frequency <= 74.116:
		note = "d'2"
	elif frequency >= 81.707 and frequency <= 83.107:
		note = "e'2"
	elif frequency >= 86.607 and frequency <= 88.007:
		note = "f'2"
	elif frequency >= 97.299 and frequency <= 98.669:
		note = "g'2"
	elif frequency >= 109.3 and frequency <= 110.7:
		note = "a'2"
	elif frequency >= 122.77 and frequency <= 124.17:
		note = "b'2"
	elif frequency >= 130.11 and frequency <= 131.51:
		note = "c'3"
	elif frequency >= 146.13 and frequency <= 147.53:
		note = "d'3"
	elif frequency >= 164.11 and frequency <= 165.51:
		note = "e'3"
	elif frequency >= 173.91 and frequency <= 175.31:
		note = "f'3"
	elif frequency >= 195.3 and frequency <= 196.7:
		note = "g'3"
	elif frequency >= 219.3 and frequency <= 220.7:
		note = "a'3"
	elif frequency >= 246.24 and frequency <= 247.64:
		note = "b'3"
	elif frequency >= 260.93 and frequency <= 262.33:
		note = "c'4"
	elif frequency >= 292.97 and frequency <= 294.37:
		note = "d'4"
	elif frequency >= 328.93 and frequency <= 330.33:
		note = "e'4"
	elif frequency >= 348.53 and frequency <= 349.93:
		note = "f'4"
	elif frequency >= 391.3 and frequency <= 392.7:
		note = "g'4"
	elif frequency >= 439.3 and frequency <= 440.7:
		note = "a'4"
	elif frequency >= 493.18 and frequency <= 494.58:
		note = "b'4"
	elif frequency >= 522.8 and frequency <= 524.2:
		note = "c'5"
	elif frequency >= 586.63 and frequency <= 588.03:
		note = "d'5"
	elif frequency >= 658.56 and frequency <= 659.96:
		note = "e'5"
	elif frequency >= 697.76 and frequency <= 699.16:
		note = "f'5"
	elif frequency >= 783.29 and frequency <= 784.69:
		note = "g'5"
	elif frequency >= 879.3 and frequency <= 880.7:
		note = "a'5"
	elif frequency >= 987.07 and frequency <= 988.47:
		note = "b'5"
	elif frequency >= 1045.8 and frequency <= 1047.2:
		note = "c'6"
	elif frequency >= 1174 and frequency <= 1175.4:
		note = "d'6"
	elif frequency >= 1317.8 and frequency <= 1319.2:
		note = "e'6"
	elif frequency >= 1396.2 and frequency <= 1397.6:
		note = "f'6"
	elif frequency >= 1567.3 and frequency <= 1568.7:
		note = "g'6"
	elif frequency >= 1759.3 and frequency <= 1760.7:
		note = "a'6"
	elif frequency >= 1974.8 and frequency <= 1976.2:
		note = "b'6"
	elif frequency >= 2092.3 and frequency <= 2093.7:
		note = "c'7"
	elif frequency >= 2348.6 and frequency <= 2350:
		note = "d'7"
	elif frequency >= 2636.3 and frequency <= 2637.7:
		note = "e'7"
	elif frequency >= 2792.3 and frequency <= 2793.7:
		note = "f'7"
	elif frequency >= 3135.3 and frequency <= 3136.7:
		note = "g'7"
	elif frequency >= 3519.3 and frequency <= 3520.7:
		note = "a'7"
	elif frequency >= 3950.4 and frequency <= 3951.8:
		note = "b'7"
	else:
		note = "c'8"
	return note
