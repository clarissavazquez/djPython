from abjad import *

def scoreFn():
	score = Score([])
	piano_staff = scoretoolds.StaffGroup([], context_name = 'PianoStaff')
	upper_staff = Staff([])
	lower_staff = Staff([])
	
	piano_staff.append(upper_staff)
	piano_staff.append(lower_staff)
	score.append(piano_staff)
	
	upper_measures = []
	upper_measures.append(Measure((2, 4), []))
	upper_measures.append(Measure((3, 4), []))
	upper_measures.append(Measure((2, 4), []))
	upper_measures.append(Measure((2, 4), []))
	upper_measures.append(Measure((2, 4), []))
	
	import copy 
	lower_measures = copy.deepcopy(upper_measures)
	
	upper_staff.extend(upper_measures)
	lower_staff.extend(lower_measures)
	
	upper_measures[0].extend("a'8 g'8 f'8 e'8")
	upper_measures[1].extend("d'4 g'8 f'8 e'8 d'8")
	upper_measures[2].extend("c'8 d'16 e'16 f'8 e'8")
	upper_measures[3].append("d'2")
	upper_measures[4].append("d'2")
	
	lower_measures[0].extend("b4 d'8 c'8")
	lower_measures[1].extend("b8 a8 af4 c'8 bf8")
	lower_measures[2].extend("a8 g8 fs8 g16 a16")
	
	upper_voice = Voice("b2", name = 'upper voice')
	command = indicatortools.LilyPondCommand('voiceOne')
	attach(command,upper_voice)
	lower_voice = Voice("b4 a4", name = 'lower voice')
	command = indicatortools.LilyPondCommand('voiceTwo')
	attach(command, lower_voice)
	lower_measures[4].extend([upper_voice, lower_voice])
	lower_measures[4].is_simultaneous = True
	
	show(score)
