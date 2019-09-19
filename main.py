import sys
import networkx as nx

from Io import *
from Graph import *

info = read(str(sys.argv[1]))
G = creategraph(info)
info_graph = featuresgraph(G)
info_nodes = featuresnodes(G)
info_edges = featuresedges(G)
out(G, info_graph, info_nodes, info_edges, str(sys.argv[1]))
degreehistogram(G)