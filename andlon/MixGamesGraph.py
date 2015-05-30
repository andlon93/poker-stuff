import matplotlib.pyplot as plt
import sessionHandler as s
##################   8-Game cash   ##################
def get_stack_from_input(line):
	index = 17
	while not line[index] == ' ': index += 1
	return float(line[17:index])

def read_cash_session_from_file(file_name):
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
		if len(all_hands) == 0: all_hands += read_cash_session_from_file(session)
		else:
			temp_result = all_hands[-1]
			new_session = read_cash_session_from_file(session)
			all_hands += [round(hand+temp_result,2) for hand in new_session]
	print 'Resultat: ', all_hands[-1], ' over ', len(all_hands), 'hender'
	return all_hands
##################   MTTs   ##################
def cashes(results):
	counter = 0
	for result in results: 
		if not result == 0.0: counter += 1
	return counter

def read_MTT_results_from_file(file_name):
	file = open(file_name, 'r')
	buy_ins = []
	results = []
	for line in file:
		buy_in, result = line.split('#')
		buy_ins.append(float(buy_in)), results.append(float(result))
	return buy_ins, results

def read_all_MTT_files():
	all_files = s.get_sessions('MTT')
	all_buy_ins = []
	all_results = []
	for file in all_files:
		buy_ins, results  = read_MTT_results_from_file(file)
		all_buy_ins += buy_ins
		all_results += results
	print 'cashet i ', 	cashes(all_results), ' av ', len(all_results), ' turneringer'
	print 'Resultat: ', sum(all_results)-sum(all_buy_ins), ' over ', len(all_buy_ins), 'turneringer'
	#make list to plot graph on
	graph_list = [all_results[0]-all_buy_ins[0]]
	for n in xrange(1, len(all_results)):
		graph_list.append( all_results[n]-all_buy_ins[n]+graph_list[n-1] )
	return graph_list


##################   plotting and main method  ##################
def plot_graph(hands):
	plt.plot(range(1,len(hands)+1),hands)
	plt.show()

def main(choice):
	#print 'cash graph: "cash". MTT graph: "MTT"'
	#choice = input()
	if choice == 'cash': plot_graph( read_all_sessions() )
	elif choice == 'MTT': plot_graph( read_all_MTT_files() )

main('MTT')