'''
Implementation of creation and analysis of substrate graph

'''

import networkx as nx

def creategraph(info):

	# Create an undirected graph
    G = nx.Graph()

    #add the nodes to the graph
    for i in range(0, int(info[0][0])):

    	G.add_node(i, pos=(int(info[i][0]), int(info[i][1])))


    #add the edges
    for i in range(int(info[0][0]) + 1, int(info[0][1])):

    	G.add_edge(int(info[i][0]), int(info[i][1]))

    return G

#Calculates topological features of nodes
def featuresnodes(G):

	info = list()
	nodes_degree = dict()

	# Calculating the degree for each node
	for i in range(0, G.number_of_nodes()):

		nodes_degree.update({i:G.degree(i)})

	info.append(nodes_degree) #Saved to list

	# Calculating the intermediation centralities

	# betweenness
	bet = nx.betweenness_centrality(G, normalized=True)

	info.append(bet) #Saved to list

	# closenness
	clo = nx.closeness_centrality(G)

	info.append(clo) #Save to list

	return info

#calculates the topological features of the edges
def featuresedges(G):

	#Calculating edge betweeness
	clo = nx.edge_betweenness_centrality(G, normalized=True, weight=None)

	return clo

#Calculates the topological characteristics of the graph
def featuresgraph(G):

	info = list()

	#Calculating Graph Density
	density = nx.density(G)

	info.append(density) #Saved to list

	#Extracting the giant component
	giant = max(nx.connected_component_subgraphs(G), key=len)

	#Calculating Graph Diameter
	diameter = nx.diameter(giant)

	info.append(diameter) #Saved to list

	return info