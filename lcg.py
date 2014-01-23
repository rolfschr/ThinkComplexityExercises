#!/usr/bin/python

### chap 6, ex 02.1 BEGIN ###
class LCG():
	def __init__(self, seed = 1, a = 1664525, c = 1013904223, m = 2**32):
		self.last = seed
		self.a = a
		self.c = c
		self.m = m

	def next(self):
		self.last = (self.a * self.last + self.c) % self.m
		return self.last
### chap 6, ex 02.1 END   ###

if __name__ == '__main__':
	lcg = LCG()
	for i in range(10):
		print lcg.next()
