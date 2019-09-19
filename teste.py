'''

Implementacao leitura e escrita de arquivos para analise topologica do grafo substrato

'''
def read(fileName): 

	file = open(fileName)

	info = list()

	subInfo = file.readline().split("\t")

	info.append(subInfo) #Salva as informacoes do numero de vertices e arestas
	subInfo = subInfo[1].split('\n')
	info[0][1] = subInfo[0]

	#Salva as informacoes dos vertices
	for i in range(0, int(info[0][0])): 

		subInfo = file.readline().split('\t')
		vertex = list()
		vertex.append(subInfo[0])
		vertex.append(subInfo[1])
		info.append(vertex)
	
	#Salva as informacoes das arestas
	for i in range(0, int(info[0][1])):

		subInfo = file.readline().split('\t')
		edge = list()
		edge.append(subInfo[0])
		edge.append(subInfo[1])
		info.append(edge)

	file.close()

	return info