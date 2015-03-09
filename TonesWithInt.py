from abjad import *
import fileinput

def extractNotes():
	f = open('musicFrequencies.txt', 'r')
	frequencies =[float(n) for n in f.read().split()]
	print frequencies
	
	pitch_numbers = [1, 2, 4, 5, 7, 9, 11, 12, 14, 16, 17]
	duration = Duration(1,8)
	note = scoretools.make_notes(pitch_numbers, duration)
	staff= Staff(note)
	show(staff)

def translateNote(frequency):
        if frequency == 27.500:
                note = "a'0"
        elif frequency == 30.868:
                note = "b'0"
        elif frequency == 32.703:
                note = "c'1"
        elif frequency == 36.708:
                note = "d'1"
        elif frequency == 41.203:
                note = "e'1"
        elif frequency == 43.654:
                note = "f'1"
        elif frequency == 48.999:
                note = "g'1"
        elif frequency == 55.000:
                note = "a'1"
        elif frequency == 61.735:
                note = "b'1"
        elif frequency == 65.406:
                note = "c'2"
        elif frequency == 73.416:
                note = "d'2"
        elif frequency == 82.407:
                note = "e'2"
        elif frequency == 87.307:
                note = "f'2"
        elif frequency == 97.999:
                note = "g'2"
        elif frequency == 110.00:
                note = "a'2"
        elif frequency == 123.47:
                note = "b'2"
        elif frequency == 130.81:
                note = "c'3"
        elif frequency == 146.83:
                note = "d'3"
        elif frequency == 164.81:
                note = "e'3"
        elif frequency == 174.61:
                note = "f'3"
        elif frequency == 196.00:
                note = "g'3"
        elif frequency == 220.00:
                note = "a'3"
        elif frequency == 246.94:
                note = "b'3"
        elif frequency == 261.63:
                note = "c'4"
        elif frequency == 293.67:
                note == "d'4"
        elif frequency == 329.63:
                note = 0
        elif frequency == 293.67:
                note == 2
        elif frequency == 329.63:
                note = 4
        elif frequency == 349.23:
                note = 5
        elif frequency == 392.00:
                note = 7
        elif frequency == 440.00:
                note = 9
        elif frequency == 493.88:
                note = 11
        elif frequency == 523.25:
                note = 12
        elif frequency == 587.33:
                note = 14
        elif frequency == 659.26:
                note = 16
        elif frequency == 698.46:
                note = 17
        elif frequency == 783.99:
                note = "g'5"
        elif frequency == 880.00:
                note = "a'5"
        elif frequency == 987.77:
                note = "b'5"
        elif frequency == 1046.5:
                note = "c'6"
        elif frequency == 1174.7:
                note = "d'6"
        elif frequency == 1318.5:
                note = "e'6"
        elif frequency == 1396.9:
                note = "f'6"
        elif frequency == 1568.0:
                note = "g'6"
        elif frequency == 1760.0:
                note = "a'6"
        elif frequency == 1975.5:
                note = "b'6"
        elif frequency == 2093.0:
                note = "c'7"
        elif frequency == 2349.3:
                note = "d'7"
        elif frequency == 2637.0:
                note = "e'7"
        elif frequency == 2793.0:
                note = "f'7"
        elif frequency == 3136.0:
                note = "g'7"
        elif frequency == 3520.0:
                note = "a'7"
        elif frequency == 3951.1:
                note = "b'7"
        elif frequency == 4186.0:
                note = "c'8"
        else:
		print "Incorrect input"
        return note

extractNotes()

