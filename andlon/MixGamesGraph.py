import matplotlib.pyplot as plt
import sessionHandler as s

debug = True

sessions = s.get_sessions()

def get_stack_from_input(line):
	index = 17
	while not line[index] == ' ': index += 1
	return float(line[17:index])

def read_session_from_file(file_name):
	file = open(file_name,'r')
	session = [ get_stack_from_input(line) for line in file if line[8:17] == 'andlon ($' ]
	
	buy_in = session[0]
	session = [ round(stack - buy_in, 2) for stack in session ]
	
	if debug: print 'sesjon: ', session
	file.close()
	return session



def plot_graph(hands):
	plt.plot(range(1,len(hands)+1),hands)
	plt.show()

plot_graph( read_session_from_file(sessions[0]) )


