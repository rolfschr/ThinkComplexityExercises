""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

from collections import deque
import random

class Vertex(object):
	"""A Vertex is a node in a graph."""

	def __init__(self, label=''):
		self.label = label

	def __repr__(self):
		"""Returns a string representation of this object that can
		be evaluated as a Python expression."""
		return 'Vertex(%s)' % repr(self.label)

	__str__ = __repr__
	"""The str and repr forms of this object are the same."""


class Edge(tuple):
	"""An Edge is a list of two vertices."""

	def __new__(cls, *vs):
		"""The Edge constructor takes two vertices."""
		if len(vs) != 2:
			raise ValueError, 'Edges must connect exactly two vertices.'
		return tuple.__new__(cls, vs)

	def __repr__(self):
		"""Return a string representation of this object that can
		be evaluated as a Python expression."""
		return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

	__str__ = __repr__
	"""The str and repr forms of this object are the same."""


class Graph(dict):
	"""A Graph is a dictionary of dictionaries.  The outer
	dictionary maps from a vertex to an inner dictionary.
	The inner dictionary maps from other vertices to edges.

	For vertices a and b, graph[a][b] maps
	to the edge that connects a->b, if it exists."""

	def __init__(self, vs=[], es=[]):
		"""Creates a new graph.  
		vs: list of vertices;
		es: list of edges.
		"""
		for v in vs:
			self.add_vertex(v)

		for e in es:
			self.add_edge(e)

	def add_vertex(self, v):
		"""Add a vertex to the graph."""
		self[v] = {}

	def add_edge(self, e):
		"""Adds and edge to the graph by adding an entry in both directions.

		If there is already an edge connecting these Vertices, the
		new edge replaces it.
		"""
		v, w = e
		self[v][w] = e
		self[w][v] = e

	def make_edge(self, v, w):
		self.add_edge(Edge(v, w))


	def get_edge(self, v, w):
		e = None
		try:
			e = self[v][w]
		except:
			pass
		return e

	def remove_edge(self, e):
		v, w = e
		if (self.get_edge(v, w) != None):
			del(self[v][w])
			del(self[w][v])

	def vertices(self):
		return self.keys()

	def edges(self):
		edges = [Edge(v, w) for v in self.keys() for w in self.keys() if w in self[v]]
#		edges = []
#		for v in self:
#			for w in self[v]:
#				e = self[v][w]
#				if (not e in edges):
#					edges.append(e)
		return edges

	def out_vertices(self, v):
		neighbors = [x for x in self[v].keys()]
#		neighbors = []
#		if (v in self):
#			neighbors = self[v].keys()
		return neighbors

	def out_edges(self, v):
		edges = [x for x in self[v].values()]
#		edges = []
#		if (v in self):
#			edges = self[v].values()
		return edges

	def add_all_edges(self):
		for v in self:
			for w in self:
				if (not w in self[v]):
					self.add_edge(v, w)
	def remove_all_edges(self):
		for v in self.keys():
			self[v] = {}

	def add_regular_edges(self, n):
		self.remove_all_edges()
		for v in self.keys():
			nbr_edges = len(self.out_edges(v))
			if (nbr_edges == n):
				continue
			i = nbr_edges
			while (i < n):
				w = random.choice(self.keys())
				if (v == w
						or len(self.out_edges(w)) == n
						or self.get_edge(v, w) != None):
					continue
				self.make_edge(v, w)
				i += 1

	# build up a regular ring lattice
	# assuming n % 2 == 0 in order to connect eacht
	# vertix to it's n nearest neighbours
	def add_regular_ring_lattice(self, n):
		self.remove_all_edges()
		vs = self.keys()
		for i in range(len(vs)):
			v = vs[i]
			for j in range(-n / 2, n / 2 + 1):
				if (j == 0):
					continue
				index = (i + j) % len(vs)
				w = vs[index]
				if (self.get_edge(v, w) == None):
					self.make_edge(v, w)






	def get_max_neighbors(self):
		num_neighbors = [len(self.out_vertices(v)) for v in self.keys()]
		return max(num_neighbors)

	def is_connected(self):
		queue = deque()
		queue.append(self.keys()[0])
		visited = []
		while (len(queue) > 0):
			v = queue.popleft()
			visited.append(v)
			for w in self.out_vertices(v):
				if (not w in visited and not w in queue):
					queue.append(w)
		return (len(visited) == len(self.keys()))


def main(script, *args):
	v = Vertex('v')
#	print v
	w = Vertex('w')
#	print w
	e = Edge(v, w)
#	print e
	g = Graph([v,w], [e])
#	print g
#	print g.get_edge(w, v)
#	g.get_edge(v, w)
	u = Vertex('u')
	g.add_vertex(u)
	print g.edges()
	print g.get_max_neighbors()
#	print g.get_edge(v, w)
#	g.remove_edge(e)
#	print g.get_edge(v, w)
#	print g.vertices()
	#print g.edges()
	#g.add_edge(Edge(w, u))
	print g.out_edges(u)


if __name__ == '__main__':
	import sys
	main(*sys.argv)
