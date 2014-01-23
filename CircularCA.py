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

if __name__ == '__main__':
	n = 10
	ca = CircularCA(50, n, ratio = 1)
	ca.start_single()
	ca.loop(n-1)

	drawer = Downey.CADrawer.PyplotDrawer()
	drawer.draw(ca)
	drawer.show()
