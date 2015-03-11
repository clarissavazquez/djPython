from abjad import *
from array import array
import fileinput

def extractNotes():
	f = open('testFrequencies.txt', 'r')
	frequencies =[float(n) for n in f.read().split()]

	variable = []	#array that will take the notes as integers
	for i in frequencies:
		tones = translateNote(i)	# will translate frequencies
		variable.append(tones)	#adds the integers to the array
	
	pitch_numbers = variable	#gits the array and get pitch
	duration = Duration(1,4)	#states the duration of the notes
	note = scoretools.make_notes(pitch_numbers, duration)	#converts integers to notes
	staff= Staff(note)	#creates a staff and sets the notes on them
	show(staff)	#shows the staff

def translateNote(frequency):
        if frequency == 27.500:
                note = -37 #A0
        elif frequency == 30.868:
                note = -36 #B0
        elif frequency == 32.703:
                note = -34 #C1
        elif frequency == 36.708:
                note = -32 #D1
        elif frequency == 41.203:
                note = -29  #E1
        elif frequency == 43.654:
                note = -32 #F1
        elif frequency == 48.999:
                note = -29 #G1
        elif frequency == 55.000:
                note = -27 #A1
        elif frequency == 61.735:
                note = -25 #B1
        elif frequency == 65.406:
                note = -24 #C2
        elif frequency == 73.416:
                note = -22 #D2
        elif frequency == 82.407:
                note = -20 #E2
        elif frequency == 87.307:
                note = -19 #F2
        elif frequency == 97.999:
                note = -17 #G2
        elif frequency == 110.00:
                note = -15 #A2
        elif frequency == 123.47:
                note = -13 #B2
        elif frequency == 130.81:
                note = -12 #C3
        elif frequency == 146.83:
                note = -10  #D3
        elif frequency == 164.81:
                note = -8 #E3
        elif frequency == 174.61:
                note = -7 #F3
        elif frequency == 196.00:
                note = -5 #G3
        elif frequency == 220.00:
                note = -3 #A3
        elif frequency == 246.94:
                note = -1 #B3
        elif frequency == 261.63:
                note = 0 #C'4
        elif frequency == 293.67:
                note == 2 #D'4
        elif frequency == 329.63:
                note = 4 #E'4
        elif frequency == 349.23:
                note == 5 #F'4
        elif frequency == 392.00:
                note = 7 #G'4
        elif frequency == 440.00:
                note = 9 #A'4
        elif frequency == 493.88:
                note = 11 #B4
        elif frequency == 523.251:
                note = 12 #C'5
        elif frequency == 587.33:
                note = 14 #D'5
        elif frequency == 659.255:
                note = 16 #E'5
        elif frequency == 698.456:
                note = 17 #F'5
        elif frequency == 783.991:
                note = 19 #G'5
        elif frequency == 880.00:
                note = 21 #A'5
        elif frequency == 987.767:
                note = 23 #B'5
        elif frequency == 1046.50:
                note = 24 #C'6
        elif frequency == 1174.66:
                note = 26 #D6
        elif frequency == 1318.51:
                note = 28 #E6
        elif frequency == 1396.91:
                note = 29 #F6
        elif frequency == 1568.0:
                note = 31 #G6
        elif frequency == 1760.0:
                note = 33 #A6
        elif frequency == 1975.5:
                note = 35 #B6
        elif frequency == 2093.0:
                note = 36 #C7
        elif frequency == 2349.3:
                note = 38 #D7
        elif frequency == 2637.0:
                note = 40 #E7
        elif frequency == 2793.0:
                note = 41 #F7
        elif frequency == 3136.0:
                note = 43 #G7
        elif frequency == 3520.0:
                note = 45 #A7
        elif frequency == 3951.1:
                note = 47 #B7
        elif frequency == 4186.0:
                note = 48 #C8
        else:
		print "Incorrect input"
        return note

extractNotes()

