import misc
from Downey.GraphWorld import *
from Graph import Vertex
from Graph import Edge
from Graph import Graph
from RG import RandomGraph
from SmallWorldGraph import SmallWorldGraph

from matplotlib import pyplot as plt
import numpy as np
import string


def testrandomcomplete(rn = 15):
	for n in range(2, rn):
		for p in range(10):
			prob = p / 10.0
			labels = string.ascii_lowercase + string.ascii_uppercase
			vs = [Vertex(c) for c in labels[:n]]
			g = RandomGraph(vs)
			g.add_random_edges(prob)
			print "%s, %s, %s" % (n, prob, g.is_connected())

### chap 4, ex 04.3 BEGIN ###
def test_clustercoefficient():

	ps = np.arange(0, 1, 0.01)
	n = 1000
	labels = string.ascii_lowercase + string.ascii_uppercase
	vs = []
	iter = misc.gen_identifier()
	for i in range(n):
		vs.append(Vertex(iter.next()))
	g = SmallWorldGraph(vs)
	g.add_regular_ring_lattice(10)
	c0 = g.get_clustering_coefficient()
	xs = []
	ys = []
	for p in ps:
		g = SmallWorldGraph(vs)
		g.add_regular_ring_lattice(10)
		g.rewire(p)
		ys.append(g.get_clustering_coefficient() / c0)
		xs.append(p)

	fig = plt.figure(dpi = 100)
	plt.subplot(1,1,1)
	plt.plot(xs, ys)
	plt.xscale('log')
	plt.show()
### chap 4, ex 04.3 END   ###



def main(script, n='20', *args):

	# create n Vertices
	n = int(n)
	labels = string.ascii_lowercase + string.ascii_uppercase
	vs = []
	iter = misc.gen_identifier()
	for i in range(n):
		vs.append(Vertex(iter.next()))
	vs = [Vertex(c) for c in labels[:n]]

	# create a graph and a layout
	g = Graph(vs)
	#g = RandomGraph(vs)
	#g.is_connected
	#g = SmallWorldGraph(vs)
	g.add_regular_ring_lattice(4)
	v = vs[0]
	print v
	print g.shortest_path(v)
	w = vs[3]
	print w
	print g.shortest_path(v, w)
	#print g.get_max_neighbors()
	#print g.get_clustering_coefficient()
	#p = 0.8
	#g.rewire(p)
	#print g.get_clustering_coefficient()
	#test_clustercoefficient()
	#g.add_random_edges(1.0)
	#print g.is_connected()

	# draw the graph
	layout = CircleLayout(g)
	gw = GraphWorld()
	gw.show_graph(g, layout)
	gw.mainloop()


if __name__ == '__main__':
	import sys
	main(*sys.argv)
	#testrandomcomplete()


