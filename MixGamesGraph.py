import matplotlib.pyplot as plt

def read_session_rom_file(file_name):
	file = open(file_name,'r')
	session = [10.0]
	session += [ float( line[17:22] ) for line in file if line[8:17] == 'andlon ($' ]
	file.close()
	return session

def plot_graph(session):
	plt.plot(range(1,len(session)+1),session)
	plt.show()
#print read_session_rom_file('HH20150527 Nasl II - $0.20-$0.40 - USD 8-Game'+'.txt')

plot_graph( read_session_rom_file('HH20150527 Nasl II - $0.20-$0.40 - USD 8-Game'+'.txt') )