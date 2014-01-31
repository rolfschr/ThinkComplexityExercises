#!/usr/bin/python

import Downey.Life as Life
import numpy


class Turmite(Life.Life):
	def __init__(self, n):
		super(Turmite, self).__init__(n, initial = None)
		m = n/2
		self.array = numpy.zeros((n, n))
		self.antx = m
		self.anty = m
		self.antd = 0 # 0 = north, 1 = e, 2 = s, 3 = west
		self.antc = 0.5 # color
		self.last_c = 0 # the color "under" the ant
 
	def step(self):
		x = self.antx
		y = self.anty
		d = self.antd
		a = self.array
		n = self.n
		tilec = self.last_c
		# turn right if current tile == white
		turn = 1 if tilec == 0 else -1
		# switch color of current tile
		tilec = (tilec + 1) % 2
		a[x, y] = tilec
		# forward ant
		d = (d + turn) % 4
		if (d == 0):
			fx = 1
			fy = 0
		elif (d == 1): #east
			fx = 0
			fy = 1
		elif (d == 2): #south
			fx = -1
			fy = 0
		else: # west
			fx = 0
			fy = -1
		self.antx = (x + fx) % n
		self.anty = (y + fy) % n
		self.antd = d
		# "draw" ant
		self.last_c = a[self.antx, self.anty]
		a[self.antx, self.anty] = self.antc

def main(script, n=20, *args):

	n = int(n)

	turmite = Turmite(30)
	viewer = Life.LifeViewer(turmite)
	viewer.animate(steps=1200)

if __name__ == '__main__':
	import sys

	profile = False
	if profile:
		import cProfile
		cProfile.run('main(*sys.argv)')
	else:
		main(*sys.argv)

