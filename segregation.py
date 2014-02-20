#!/usr/bin/python

import numpy as np
import matplotlib
import matplotlib.pyplot as pyplot

### chap 10, ex 01 BEGIN ###
class Segregation(object):
	def __init__(self, n, empty_p = 0.1, num_happy = 5):
		self.array = np.random.random_integers(1, 2, (n, n))
		self.num_happy = num_happy
		self.empty = set()
		self.happy_agent = []
		i = int((n*n) * empty_p)
		j = 2*i
		while (i > 0):
			x, y = np.random.random_integers(0, n-1, 2)
			if (self.array[x, y] != 0):
				self.array[x, y] = 0
				i -= 1
				self.empty.add((x,y))
			j -= 1
			if (j == 0):
				break # never trive more than doubled i

	@property
	def n(self):
		return self.array.shape[0]

	def step(self):
		while (True):
			x, y = np.random.random_integers(0, self.n-1, 2)
			if ((x, y) not in self.empty):
				break
		if (not self.is_happy(x, y)):
			nx, ny = self.empty.pop()
			self.array[nx, ny] = self.array[x, y]
			self.array[x, y] = 0
			self.empty.add((x,y))
			self.happy_agent.append(0)
		else:
			self.happy_agent.append(1)

	def is_happy(self, x, y, c = None):
		if c == None:
			c = self.array[x, y]
		s = self.array[max(0, x-1):x+2,max(0, y-1):y+2]
		si = (s == c).astype(int)
		return np.sum(si) - 1 >= self.num_happy

	def loop(self, steps = 10000):
		#fig = pyplot.figure()
		pyplot.axis([0, self.n, 0, self.n])
		pyplot.xticks([])
		pyplot.yticks([])
		pyplot.pcolor(self.array, cmap=matplotlib.cm.Blues)
		pyplot.savefig('a.png')
		pyplot.close()
		for i in range(steps):
			self.step()
		pyplot.pcolor(self.array, cmap=matplotlib.cm.Blues)
		pyplot.savefig('b.png')
		pyplot.close()
		cha = np.cumsum(self.happy_agent)
		l = len(cha)
		chap = [a/float(l) for a in cha]
		pyplot.plot(chap)
		pyplot.title("probability to find an happy agent at a random location (in %)")
		pyplot.savefig('c.png')
### chap 10, ex 01 END   ###

### chap 10, ex 02 BEGIN ###
class SegregationBishop(Segregation):
	def __init__(self, n, empty_p = 0.1, num_happy = 5, new_neighbors = 0.7):
		super(SegregationBishop, self).__init__(n, empty_p, num_happy)
		self.new_neighbors = new_neighbors

	def step(self):
		while (True):
			x, y = np.random.random_integers(0, self.n-1, 2)
			if ((x, y) not in self.empty):
				break
		if (self.is_happy(x, y)): # measure prob to find a happy agent
			self.happy_agent.append(1)
		else:
			self.happy_agent.append(0)
		nx, ny = self.empty.pop()
		if (self.is_happy(nx, ny, self.array[x, y])
				or np.random.random > self.new_neighbors):
			# move if a) new like new neighbors or b) don't fore small fraction of agents
			self.array[nx, ny] = self.array[x, y]
			self.array[x, y] = 0
			self.empty.add((x,y))
		else:
			# else, dont move
			self.empty.add((nx,ny))
### chap 10, ex 02 END   ###

if __name__ == '__main__':
	s = Segregation(100, 0.1, num_happy = 5)
	s = SegregationBishop(100, 0.1, num_happy = 2)
	s.loop(100000)
