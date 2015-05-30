##################   Filename of each session   ##################
MTTs = ['MTTs_05.2015']
sessions = ['$10_8-Game_2015.05.27',
			'$10_8-Game_2015.05.28_01','$10_8-Game_2015.05.28_02','$10_8-Game_2015.05.28_03',
			'$10_8-Game_2015.05.29_01','$10_8-Game_2015.05.29_02','$10_8-Game_2015.05.29_03','$10_8-Game_2015.05.29_04']
##################   return list with all sessions   ##################

def get_sessions(choice):
	all_sessions = []
	if choice == 'cash':
		for session in sessions:
			all_sessions.append( session + '.txt' )
	elif choice == 'MTT':
		for MTT in MTTs:
			all_sessions.append( MTT + '.txt' )
	return all_sessions