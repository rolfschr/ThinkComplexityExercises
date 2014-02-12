import re, string, cmath, math
import Downey.Pmf as Pmf
import Downey.Cdf as Cdf
import matplotlib.pyplot as pyplot
import numpy as np

### chap 2, ex 07 BEGIN ###
def gen_identifier():
	i = 1
	while (True):
		for c in string.lowercase:
			yield "%s%s" % (c, i)
		i += 1
### chap 2, ex 07 END   ###

### chap 3, ex 03 BEGIN ###
def bisect(t, ls, start = 0, end = None):
	if (len(ls) == 1):
		if (ls[0] == t):
			return start
		else:
			return None
	if (end == None):
		end = len(ls) - 1
	i = (end - start) / 2 + start
	if (i == 0):
		i = start
	print i
	v = ls[i]
	print v
	print "e: %s" % end
	if (t == v):
		return i
	elif (i == 0):
		return None
	elif (t < v):
		return bisect(t, ls, start, i-1)
	else:
		return bisect(t, ls, i+1, end)
### chap 3, ex 03 END   ###

### chap 5, ex 01 BEGIN ###
def zipf(filename):
	words = __zipf_get_words(filename)
	hist = Pmf.MakeHistFromList(words)
	return hist

def __zipf_get_words(filename):
	try:
		with open(filename, 'r') as f:
			for line in f:
				text = re.sub(r'([^\s\w]|_)+', '', line)
				text = text.lower()
				text = text.rstrip().split()
				for word in text:
					yield word
	except IOError:
		pass

def zipf_print(hist):
	ls = sorted(hist.GetDict(), key=hist.GetDict().get, reverse = True)
	for word in ls:
		print word

def zipf_plot(hist):
	fs = sorted(hist.Freqs(), reverse = True)
	rs = [i for i in range(1, len(fs) + 1)]
	pyplot.plot(rs, fs)
	scale = 'log'
	pyplot.xscale(scale)
	pyplot.yscale(scale)
	pyplot.title('')
	pyplot.xlabel('rank')
	pyplot.ylabel('freqs')
	pyplot.show()

### chap 5, ex 01 END   ###

### chap 5, ex 03 BEGIN ###
### chap 5, ex 04 BEGIN ###
def plot_ccdf(xs, xscale = 'linear', yscale = 'log'):
	xs = sorted(xs)
	cdf = Cdf.MakeCdfFromList(xs)
	ys = [1 - cdf.Prob(x) for x in xs]
	pyplot.plot(xs, ys)
	pyplot.xscale(xscale)
	pyplot.yscale(yscale)
	pyplot.xlabel('value (%s)' % xscale)
	pyplot.ylabel('prob (%s)' % yscale)
	pyplot.show()

### chap 5, ex 03 END   ###
### chap 5, ex 04 END   ###

### chap 5, ex 05 BEGIN ###
def pop_dist(filename = 'pops.txt'):
	with open(filename) as f:
		pops = map(lambda s: int(s.rstrip()), f.readlines())
		cdf = Cdf.MakeCdfFromList(pops)
		xs, ps = cdf.Render()
		pyplot.plot(xs, ps)
		pyplot.xlabel('value')
		pyplot.ylabel('prob')
		pyplot.show()
		pyplot.plot(xs, ps)
		pyplot.xscale('log')
		pyplot.xlabel('value')
		pyplot.ylabel('prob')
		pyplot.show()
		plot_ccdf(pops, xscale = 'log', yscale = 'log')

### chap 5, ex 05 END   ###

### chap 9, ex 02 BEGIN ###
def H(h, n):
	N = len(h)
	H = 0
	i = complex(0, 1)
	W = cmath.exp(2 * math.pi * i * n / N)
	for k in range(N):
		H += h[k] * (W ** k)
	return H

def dft(h):
	N = len(h)
	Hn = []
	for n in range(0, N):
		Hn.append(H(h, n))
	return Hn
### chap 9, ex 02 END   ###

def main(script, *args):
	h = np.random.random(100)
	Hn = dft(h)


if __name__ == '__main__':
	import sys
	main(*sys.argv)
