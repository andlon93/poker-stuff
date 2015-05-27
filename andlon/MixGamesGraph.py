import matplotlib.pyplot as plt
import sessionHandler as s

sessions = s.get_sessions()

def read_session_from_file(file_name):
	file = open(file_name,'r')
	session = [10.0]
	session += [ float( line[17:22] ) for line in file if line[8:17] == 'andlon ($' ]
	file.close()
	return session

def plot_graph(session):
	plt.plot(range(1,len(session)+1),session)
	plt.show()

plot_graph( s.get_sessions() )

