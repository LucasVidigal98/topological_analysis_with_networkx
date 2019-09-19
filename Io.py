'''

File reading and writing implementation for substrate graph topological analysis

'''

import networkx as nx
import collections
import matplotlib.pyplot as plt

def read(file_name): 

	file = open(file_name)

	info = list()

	sub_info = file.readline().split("\t")

	info.append(sub_info) #Saves the number of vertices and edges information
	sub_info = sub_info[1].split('\n')
	info[0][1] = sub_info[0]

	#Saves as nodes information
	for i in range(0, int(info[0][0])): 

		sub_info = file.readline().split('\t')
		node = list()
		node.append(sub_info[0])
		node.append(sub_info[1])
		node.append(vertex)
	
	#Saves as edges information
	for i in range(0, int(info[0][1])):

		sub_info = file.readline().split('\t')
		edge = list()
		edge.append(sub_info[0])
		edge.append(sub_info[1])
		info.append(edge)

	file.close()

	return info

def out(G, info_graph, info_nodes, info_edges, file_name):

	file_name_out = file_name[:(len(file_name)-4)] + ".info"

	out_file = open(file_name_out, "w")

	#Graph Properties
	out_file.write("Graph:\n")
	line = "Density\t" + "Diameter\n" 
	out_file.write(line)
	line = str(info_graph[0]) + "\t\t" + str(info_graph[1])+ "\n"
	out_file.write(line + "\n")

	#Nodes Properties
	out_file.write("Nodes:\n")
	line = "Node\t" + "Degree\t" + "Betweeness\t" + "Closeness\n"
	out_file.write(line)

	for i in range(0, G.number_of_nodes()):

		line = str(i) + "\t\t" + str(info_nodes[0][i]) + "\t" + str(info_nodes[1][i]) + "\t" + str(info_nodes[2][i]) + "\n"
		out_file.write(line)

	out_file.write("\n")

	#Edges Properties
	out_file.write("Edges: \n")
	line = "Edge\t" + "Betweeness\n"
	out_file.write(line)

	for edge in G.edges():

		line = str(edge)+ "\t" + str(info_edges[edge]) + "\n"
		out_file.write(line)


	out_file.close()

def degreehistogram(G):

	degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
	# print "Degree sequence", degree_sequence
	degreeCount = collections.Counter(degree_sequence)
	deg, cnt = zip(*degreeCount.items())

	fig, ax = plt.subplots()
	plt.bar(deg, cnt, width=0.80, color='b')

	plt.title("Degree Histogram")
	plt.ylabel("Count")
	plt.xlabel("Degree")
	ax.set_xticks([d + 0.4 for d in deg])
	ax.set_xticklabels(deg)

	# draw graph in inset
	plt.axes([0.4, 0.4, 0.5, 0.5])
	Gcc = sorted(nx.connected_component_subgraphs(G), key=len, reverse=True)[0]
	pos = nx.spring_layout(G)
	plt.axis('off')
	nx.draw_networkx_nodes(G, pos, node_size=20)
	nx.draw_networkx_edges(G, pos, alpha=0.4)

	plt.show()
