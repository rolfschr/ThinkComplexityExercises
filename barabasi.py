#!/usr/bin/python

import Graph
import Downey.GraphWorld as dgw
import Downey.Pmf as Pmf
import random, bisect
import matplotlib.pyplot as pyplot

# crap
		#ws_weights = map(lambda w: float(g.get_degree(w)) / sum_degrees, ws)
		#ws_weights = [sum(ws_weights[:i]) for i in range(1, len(ws_weights)+1)] # cumulative sum
		#w = ws[bisect.bisect_left(ws_weights, random.random())]

### chap 5, ex 03.1 BEGIN   ###
def get_graph(m0 = 5, m0e = 1, m = 5, t = 2, debug = True):
	g = Graph.Graph()
	# create initial nodes
	for i in range(m0):
		v = Graph.Vertex(str(i))
		g.add_vertex(v)
	# make initial graph complete
	if (m0e == -1):
		g.add_all_edges()
	# create at least m0e initial edges for each node
	else:
		vertices = g.vertices()
		for i in range(m0):
			for j in range(m0e):
				v = vertices[i]
				w = v
				while (w == v):
					w = random.choice(g.vertices())
				g.make_edge(v, w) # might override old edges ...
	# build network
	ws = g.vertices()
	sum_degrees = sum([g.get_degree(w) for w in ws]) / 2
	degrees = {}
	for w in ws:
		degrees[w] = float(g.get_degree(w))
	for i in range(t):
		v = Graph.Vertex(str(i + m0))
		j = 0
		edges = []
		ws = g.vertices()
		for j in range(m):
			r = random.random()
			prob = 0
			for w in ws:
				prob += degrees[w] / sum_degrees
				if (r <= prob):
					e = Graph.Edge(v, w)
					# this will 'probably' not add m nodes during the first iterations ...
					# which results in some strange plot, heck the paper is not concise :/
					if (e not in edges):
						edges.append(e)
						degrees[w] += 1
						sum_degrees += 1
					break

		g.add_vertex(v)
		g.add_edges(edges)
		degrees[v] = float(len(edges))
		if (debug and i % 1000 == 0):
			print i
	return g

def plot(g, show = False):
	if (show):
		layout = dgw.CircleLayout(g)
		gw = dgw.GraphWorld()
		gw.show_graph(g, layout)
		gw.mainloop()
	hist = Pmf.MakeHistFromList(g.get_degrees())
	k, pk = zip(*(sorted(hist.Items())))
	#print k, pk
	pyplot.plot(k, pk)
	scale = 'log'
	#scale = 'linear'
	pyplot.xscale(scale)
	pyplot.yscale(scale)
	pyplot.title('P(k) vs k')
	pyplot.xlabel('k')
	pyplot.ylabel('P(k)')
	pyplot.show()


def main(script, *args):
	plot(get_graph(m0e = -1, t = 150000), show = False)

if __name__ == '__main__':
	import sys
	main(*sys.argv)
