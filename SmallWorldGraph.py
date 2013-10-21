
from Graph import *
from RG import *
import random

class SmallWorldGraph(RandomGraph):

	def rewire(self, p):
		# assume we start with a regular graph

		# first, save all original edges
		edges_per_v = {}
		for v in self.keys():
			edges_per_v[v] = self.out_edges(v)

		for i in range(len(self.values()[0])):
			print i
			already_considered = []
			for v in self.keys():
				e = edges_per_v[v][i]
				if (not e in already_considered): # prevent using the same edge twice
					if (random.random() <= p):
						# remvoe edge and make new one
						self.remove_edge(e)
						print v
						while(True):
							w = random.choice(self.keys())
							if (w != v and self.get_edge(v, w) == None):
								break
						self.make_edge(v, w)
					already_considered.append(e)

		#print p
