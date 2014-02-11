#!/usr/bin/python

import Downey.Life as Life
import Downey.Pmf as Pmf
import numpy as np
import matplotlib.pyplot as pyplot

### chap 9, ex 01 BEGIN ###
class Sandpile(Life.Life):
	def __init__(self, n, K = 10):
		super(Sandpile, self).__init__(n)
		self.K = K
		self.array = np.random.random_integers(K-3, K, (n, n))
		self.clean_limits()
		self.sizes = []
		self.n = n

	def clean_limits(self):
		self.array[0,] = 0
		self.array[self.n-1,] = 0
		self.array[0:,0] = 0
		self.array[0:,self.n-1] = 0

	def stabilize_rek(self):
		return self.perturb(1, 1, 0)

	def perturb_rek(self, x, y, inc):
		a = self.array
		ret = set()
		if x == 0 or y == 0 or x == self.n-1 or y == self.n-1:
			a[x, y] = 0
		else:
			a[x, y] += inc
			ret.add((x, y))
			if a[x, y] > self.K:
				a[x, y] -= 4
				ret |= self.perturb_rek(x-1, y, +1)
				ret |= self.perturb_rek(x+1, y, +1)
				ret |= self.perturb_rek(x, y-1, +1)
				ret |= self.perturb_rek(x, y+1, +1)
		# return set of all modified sites
		return ret

	def stabilize_iter(self):
		ret = set()
		for x in range(1, self.n-2):
			for y in range(1, self.n-2):
				if self.array[x, y] > self.K:
					self.dec(x, y)
					ret.dd((x, y))



	def dec(self, x, y):
		a = self.array
		if x == 0 or y == 0 or x == self.n-1 or y == self.n-1:
			a[x, y] = 0
		else:
			a[x, y] -= 4
			a[x-1, y] += 1
			a[x+1, y] += 1
			a[x, y-1] += 1
			a[x, y+1] += 1
			self.clean_limits()



	def step(self):
		x, y = np.random.random_integers(1, self.n-2, 2)
		self.sizes.append(len(self.perturb_rek(x, y, 1)))
### chap 9, ex 01 END   ###


def main(script, n=3, K = 10, *args):

	n = int(n)
	K = int(K)

	sp = Sandpile(n, K)
	#sp.stabilize()
	#viewer = Life.LifeViewer(sp)
	#viewer.animate(steps=200)
	sp.loop(2000)
	print sp.sizes
	pmf = Pmf.MakePmfFromList(sp.sizes)
	#pmf = Pmf.MakeHistFromList(sp.sizes)
	xs, ys = pmf.Render()
	print xs, ys
	pyplot.plot(xs, ys, 'ro')
	dim, _ = np.polyfit(np.log(xs), np.log(ys), 1)
	print dim
	lx = range(1, max(xs))
	ly = [x**(dim) for x in lx]
	pyplot.plot(lx, ly)
	scale = 'log'
	pyplot.xscale(scale)
	pyplot.yscale(scale)
	pyplot.xlabel('value')
	pyplot.ylabel('prob')
	pyplot.show()



if __name__ == '__main__':
	import sys

	profile = False
	if profile:
		import cProfile
		cProfile.run('main(*sys.argv)')
	else:
		main(*sys.argv)

