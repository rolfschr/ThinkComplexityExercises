#!/usr/bin/python

from Downey.CA import CA
import Downey.CADrawer

### chap 6, ex 01 BEGIN ###
class CircularCA(CA):

	def step(self):
		"""Executes one time step by computing the next row of the array."""
		i = self.next
		self.next += 1

		a = self.array
		t = self.table
		for j in xrange(self.m):
			l = (j-1) if j != 0 else self.m-1
			r = (j+1) if j != self.m-1 else 0
			tup = tuple([a[i-1, l], a[i-1, j], a[i-1, r]])
			a[i,j] = t[tup]
### chap 6, ex 01 END   ###

### chap 6, ex 03.1 BEGIN ###
def ex631():
	n = 2**8
	rule = 110
	ratio = 2
	ca = CA(rule, n, ratio = ratio)
	#m = ratio * n / 2
	#start = 1
	#end = start + 100
	#for i in range(start, end, 3):
	#	ca.array[0, i] = 0
	#	ca.array[0, i+1] = 1
	#	ca.array[0, i+2] = 0
	#ca.next += 1
	ca.start_random()
	ca.loop(n-1)
	return ca
### chap 6, ex 03.1 END   ###

### chap 6, ex 03.2 BEGIN ###
def ex632():
	n = 2**8
	rule = 110
	ratio = 2
	ca = CA(rule, n, ratio = ratio)
	#ca.start_random()
	m = ratio * n / 2
	ca.array[0, m-1] = 1
	ca.array[0, m] = 1
	for i in range(20):
		ca.array[0, m+i] = 1
	ca.start_single()
	ca.loop(n-1)
	return ca
### chap 6, ex 03.2 END   ###

if __name__ == '__main__':
	ca = ex631()

	drawer = Downey.CADrawer.PyplotDrawer()
	drawer.draw(ca)
	drawer.show()
