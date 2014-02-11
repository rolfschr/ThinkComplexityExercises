#!/usr/bin/python

import Downey.Life as Life
import numpy


empty, tree, fire = (0, 1, 2)

### chap 8, ex 02 BEGIN ###
class ForestFire(Life.Life):
	def __init__(self, n, p, f):
		super(ForestFire, self).__init__(n, initial = "random")
		self.p = p
		self.array = numpy.random.random_integers(0, 1, (n, n))

	def step(self):
		a = self.array
		new_a = numpy.zeros((self.n, self.n), numpy.int8)
		for i in range(self.n):
			for j in range(self.n):
				if a[i, j] == fire:
					new_a[i, j] = empty
				elif a[i, j] == empty:
					new_a[i, j] = tree if numpy.random.random() <= self.p else empty
				else: # cell is a tree
					new_a[i, j] = fire if self.should_burn(i, j) else tree
		self.array = new_a

	def should_burn(self, i, j):
		# a tree is going to burn if any neighbour burns or with prob f
		for x in range(i-1, i+2):
			for y in range(j-1, j+2):
				try:
					if (self.array[x, y] == fire):
						return True
				except IndexError:
					pass
		return numpy.random.random() <= self.f
### chap 8, ex 02 END   ###

def main(script, n=20, p = 0.01, f = 0.001, *args):

	n = int(n)
	p = float(p)
	f = float(f)

	forest = ForestFire(n, p, f)
	viewer = Life.LifeViewer(forest)
	viewer.animate(steps=1000)


if __name__ == '__main__':
	import sys

	profile = False
	if profile:
		import cProfile
		cProfile.run('main(*sys.argv)')
	else:
		main(*sys.argv)

