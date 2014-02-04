#!/usr/bin/python

from Downey.CA import CA
from Downey.CADrawer import PyplotDrawer
import matplotlib.pyplot as pyplot
import numpy as np

### chap 8, ex 01 BEGIN ###
def fractal_dim(ca_rule, t = 100, plot = True):
	""" plot box counting dimension and return estimated dimension"""
	ca = CA(ca_rule, t)
	ca.start_single()
	Ns = [1]
	drawer = PyplotDrawer()
	for i in range(t-1):
		ca.step()
		Ns.append(sum(ca.array[ca.next-1]))
	Ns = np.cumsum(Ns)
	one_over_eps = range(1, ca.n + 1)
	dim, _ = np.polyfit(np.log(one_over_eps), np.log(Ns), 1)
	if (plot):
		pyplot.plot(one_over_eps, Ns)
		scale = 'log'
		pyplot.xscale(scale)
		pyplot.yscale(scale)
		pyplot.title('')
		pyplot.xlabel('1/eps')
		pyplot.ylabel('N(eps)')
		pyplot.show()
		drawer.draw(ca)
		drawer.show()
	return dim
### chap 8, ex 01 END   ###


if __name__ == '__main__':
	print fractal_dim(18, 64, plot = False)
