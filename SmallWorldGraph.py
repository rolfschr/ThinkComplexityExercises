
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
			already_considered = []
			for v in self.keys():
				e = edges_per_v[v][i]
				if (not e in already_considered): # prevent using the same edge twice
					if (random.random() <= p):
						# remvoe edge and make new one
						self.remove_edge(e)
						while(True):
							w = random.choice(self.keys())
							if (w != v and self.get_edge(v, w) == None):
								break
						self.make_edge(v, w)
					already_considered.append(e)

		#print p
	def get_clustering_coefficient(self):
		cvs = []
		for v in self.keys():
			cvs.append(self.local_clustering_coefficient(v))
		mean = sum(cvs) / float(len(cvs))
		return mean

	def local_clustering_coefficient(self, v):
		neighbors = self.out_vertices(v)
		maxi = len(neighbors) * (len(neighbors) - 1) / 2
		if (maxi == 0):
			return 0
		cv = 0
		for n in neighbors:
			for m in neighbors:
				if (n != m):
					if (m in self[n]): # edge exists
						cv += 1
		if (cv > 0):
			cv /= 2 # dont count edges twice
		return cv / float(maxi)
