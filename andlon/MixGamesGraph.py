import matplotlib.pyplot as plt
import sessionHandler as s

def get_stack_from_input(line):
	index = 17
	while not line[index] == ' ': index += 1
	return float(line[17:index])

def read_session_from_file(file_name):
	file = open(file_name,'r')
	session = [ get_stack_from_input(line) for line in file if line[8:17] == 'andlon ($' ]
	
	buy_in = session[0]
	session = [ round(stack - buy_in, 2) for stack in session ]
	
	file.close()
	return session

def read_all_sessions():
	sessions = s.get_sessions()
	all_hands = []
	for session in sessions:
		print session
		if len(all_hands) == 0: all_hands += read_session_from_file(session)
		else:
			temp_result = all_hands[-1]
			new_session = read_session_from_file(session)
			all_hands += [round(hand+temp_result,2) for hand in new_session]
	print 'Resultat: ', all_hands[-1], ' over ', len(all_hands), 'hender'
	return all_hands

def plot_graph(hands):
	plt.plot(range(1,len(hands)+1),hands)
	plt.show()

plot_graph( read_all_sessions() )