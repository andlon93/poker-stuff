##################   Filename of each session   ##################
sessions = ['session']
##################   return list with all sessions   ##################

def get_sessions():
	all_sessions = []
	for session in sessions:
		all_sessions.append( session + '.txt' )
	#print len(all_sessions), 'hender over', len(sessions), 'sesjoner'
	return all_sessions

