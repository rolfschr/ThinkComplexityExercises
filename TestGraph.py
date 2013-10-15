import string
from GraphWorld import *
from Graph import Vertex
from Graph import Edge
from Graph import Graph
from RandomGraph import RandomGraph

def testrandomcomplete(rn = 15):
	for n in range(2, rn):
		for p in range(10):
			prob = p / 10.0
			labels = string.ascii_lowercase + string.ascii_uppercase
			vs = [Vertex(c) for c in labels[:n]]
			g = RandomGraph(vs)
			g.add_random_edges(prob)
			print "%s, %s, %s" % (n, prob, g.is_connected())


def main(script, n='10', *args):

	# create n Vertices
#	n =20
	n = int(n)
	labels = string.ascii_lowercase + string.ascii_uppercase
	vs = [Vertex(c) for c in labels[:n]]

	# create a graph and a layout
	#g = Graph(vs)
	g = RandomGraph(vs)
	#g.add_regular_edges(3)
	g.add_random_edges(1.0)
	print g.is_connected()
	layout = CircleLayout(g)

	# draw the graph
	gw = GraphWorld()
	gw.show_graph(g, layout)
	gw.mainloop()


if __name__ == '__main__':
	import sys
	#main(*sys.argv)
	testrandomcomplete()


