import string, random
from Graph import Vertex
from Graph import Edge
from Graph import Graph

class RandomGraph(Graph):
	def __init__(self, label=''):
		Graph.__init__(self, label)

### chap 2, ex 04 BEGIN ###
	def add_random_edges(self, p):
		for i, v in enumerate(self.vertices()):
			for j, w in enumerate(self.vertices()):
				if (j <= i): continue
				if (random.random() <= p):
					self.make_edge(v, w)
### chap 2, ex 04 END   ###
