### chap 4, ex 01 BEGIN ###
class FIFO(object):

	def __init__(self, bufsize = 4):
		self.bufsize = bufsize
		self.buf = []
		for i in range(bufsize):
			self.buf.append(None)
		self.start = 0
		self.end = 0

	def append(self, v):
		self.buf[self.end] = v
		self.end = (self.end + 1) % self.bufsize
		if (self.end == self.start):
			self.start = (self.end + 1) % self.bufsize # discard oldest element
		return self

	def pop(self):
		if (self.is_empty()):
			return None
		else:
			v = self.buf[self.start]
			self.start = (self.start + 1) % self.bufsize
			return v

	def is_full(self):
		return (self.end + 1 % self.bufsize == self.start)

	def is_empty(self):
		return (self.end == self.start)

	def __str__(self):
		out = []
		out.append("start: %s, end: %s" % (self.start, self.end))
		out.append("buffer: %s" % (self.buf))
		return '\n'.join(out)
### chap 4, ex 01 END   ###


def main(script):
	f = FIFO()
	print f
	f.append(3)
	print f
	f.append(4)
	f.append(5)
	print f
	print f.pop()
	print f
	print f.pop()
	print f
	print f.pop()
	print f
	print f.pop()
	print f
	print '---------------'
	f.append(1).append(2).append(3).append(4).append(5)
	print f


if __name__ == '__main__':
	import sys
	main(*sys.argv)
