#!/usr/bin/env python

import operator, re, math
import matplotlib.pyplot as pyplot

### chap 5, ex 01 BEGIN ###
class Hist(object):
	def __init__(self):
		self.clean()

	def clean(self):
		self.word2freq = {}
		self.word2rank = {}
		self.ordered_by_rank = []
		self.dirty = True

	def add_word(self, word):
		self.dirty = True
		if (word in self.word2freq):
			self.word2freq[word] = self.word2freq[word] + 1
		else:
			self.word2freq[word] = 1

	def add_text(self, text):
		p = re.compile("[\w\s]")
		s = ''.join(e for e in text if p.match(e))
		s = re.sub("\s\s+", " ", s)
		for word in s.split(' '):
			self.add_word(word)

	def add_file(self, filename):
		f = open(filename, "r")
		for text in f:
			if (text != '\n'):
				self.add_text(text.strip())
		f.close()

	def update(self):
		if (self.dirty):
			# index = rank
			sorted_by_rank = sorted(self.word2freq.iteritems(), key=operator.itemgetter(1), reverse = True)
			for i in range(len(sorted_by_rank)):
				word, freq = sorted_by_rank[i]
				self.word2rank[word] = i + 1
				self.ordered_by_rank.append(word)
			self.dirty = False

	def get_rank(self, w):
		self.update()
		return self.word2rank[w]

	def get_frequency(self, w):
		return self.word2freq[w]

	def get_as_ordered_list(self):
		self.update()
		return self.ordered_by_rank


	def plot(self):
		self.update()
		xs = [math.log(x+1) for x in range(len(self.ordered_by_rank))]
		ys = [math.log(self.get_rank(x)) for x in self.ordered_by_rank]
		print xs, ys
		#pyplot.plot(xs, ys, color = 'r', marker = 'o')
		pyplot.plot(xs, ys, 'rD')
		scale = 'log'
		pyplot.xscale(scale)
		pyplot.yscale(scale)
		pyplot.title('')
		pyplot.xlabel('log r')
		pyplot.ylabel('log f')
		pyplot.show()
### chap 5, ex 01 END   ###

if __name__ == '__main__':
	h = Hist()
	h.add_file('alice_wonderland_gutenberg.txt')
	#h.add_file('a.txt')
	print h.get_rank('the')
	print h.get_frequency('the')
	print h.get_as_ordered_list()
	h.plot()
