import matplotlib.pyplot as plt

def read_session_rom_file(file_name):
	file = open(file_name,'r')
	session = [10.0]
	session += [float(line[15:21] for line in file if line[5:14])]
	close(file_name)
	return session

def plot_graph(session):
	plt.plot(range(1,len(session)+1),session)
	plt.show()

plot_graph( read_session_rom_file('') )