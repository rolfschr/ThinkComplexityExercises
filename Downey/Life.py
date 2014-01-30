""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

import numpy
import scipy.ndimage

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as pyplot


class Life(object):
	"""Implements Conway's Game of Life.

	n:     the number of rows and columns
	"""

	def __init__(self, n, mode='wrap', initial=None):
		"""Attributes:
		n:      number of rows and columns
		mode:   how border conditions are handled
		array:  the numpy array that contains the data.
		weights: the kernel used for convolution
		"""
		self.n = n
		self.mode = mode
		if initial == "random":
			self.array = numpy.random.random_integers(0, 1, (n, n))
		else:
			self.array = numpy.zeros((n, n), numpy.int8)
		if initial == "r":
			m = n / 2
			#array[row, col]
			self.array[m-1, m] = 1
			self.array[m, m] = 1
			self.array[m, m-1] = 1
			self.array[m+1, m] = 1
			self.array[m+1, m+1] = 1

		self.weights = numpy.array([[1,1,1],
			[1,10,1],
			[1,1,1]])

	def add_glider(self, x=0, y=0):
		coords = [(0,1), (1,2), (2,0), (2,1), (2,2)]
		for i, j in coords:
			self.array[x+i, y+j] = 1

	def loop(self, steps=1):
		"""Executes the given number of time steps."""
		[self.step() for i in xrange(steps)]

	def step(self):
		"""Executes one time step."""
		con = scipy.ndimage.filters.convolve(self.array, 
				self.weights,
				mode=self.mode)

		boolean = (con==3) | (con==12) | (con==13)
### chap 7, ex 01 BEGIN(1) ###
		self.last_array = self.array
		self.array = numpy.int8(boolean)
		if ((self.array == self.last_array).all()):
			return False
		return True
### chap 7, ex 01 END(1)   ###

### chap 7, ex 03 BEGIN ###
	def readPlaintext(self, filename, init_x = 10, init_y = 10):
		with open(filename) as f:
			lines = f.readlines()
			x = init_x
			for line in lines:
				if (not line.startswith("!")):
					y = init_y
					for c in line.strip():
						if (c != "."):
							self.array[x, y] = 1
						y += 1
				x += 1
### chap 7, ex 03 END   ###

class LifeViewer(object):
	"""Generates an animated view of the grid."""
	def __init__(self, life, cmap=matplotlib.cm.Blues):
		self.life = life
		self.cmap = cmap

		self.fig = pyplot.figure()
		pyplot.axis([0, life.n, 0, life.n])
		pyplot.xticks([])
		pyplot.yticks([])

		self.pcolor = None
		self.update()

	def update(self):
		"""Updates the display with the state of the grid."""
		if self.pcolor:
			self.pcolor.remove()

		a = self.life.array
		self.pcolor = pyplot.pcolor(a, cmap=self.cmap)
		self.fig.canvas.draw()

	def animate(self, steps=10):
		"""Creates the GUI and then invokes animate_callback.

		Generates an animation with the given number of steps.
		"""
		self.steps = steps
		self.fig.canvas.manager.window.after(1000, self.animate_callback)
		pyplot.show()

	def animate_callback(self):
		"""Runs the animation."""
		for i in range(self.steps):
			ret = self.life.step()
			self.update()
### chap 7, ex 01 BEGIN(2) ###
			if (not ret):
				break
			print i
### chap 7, ex 01 END(2)   ###


def main(script, n=20, *args):

	n = int(n)

	life = Life(n, initial = None)
	#life.add_glider()
	life.readPlaintext("Downey/puffer1.cells")
	viewer = LifeViewer(life)
	viewer.animate(steps=1000)


if __name__ == '__main__':
	import sys

	profile = False
	if profile:
		import cProfile
		cProfile.run('main(*sys.argv)')
	else:
		main(*sys.argv)
