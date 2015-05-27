##################   Filename of each session   ##################
sessions = ['HH20150527 Nasl II - $0.20-$0.40 - USD 8-Game',
			'HH20150527 Nasl II - $0.20-$0.40 - USD 8-Game (copy)'
																	]
##################   return list with all sessions in plotable format   ##################
def read_session_from_file(file_name):
	file = open(file_name,'r')
	session = [10.0]
	session += [ float( line[17:22] ) for line in file if line[8:17] == 'andlon ($' ]
	file.close()
	return session

def get_sessions():
	plotable_sessions = []
	for session in sessions:
		plotable_sessions += read_session_from_file(session+'.txt')
	print len(plotable_sessions), 'hender over', len(sessions), 'sesjoner'
	return plotable_sessions

