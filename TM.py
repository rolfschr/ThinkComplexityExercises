#!/usr/bin/python

from Downey.CA import CA
import Downey.CADrawer

### chap 6, ex 04 BEGIN ###
# 3 state busy beaver
# states
SA = 'A'
SB = 'B'
SC = 'C'
SH = 'HALT'
# movements
ML = 'L'
MR = 'R'
# action table
AT = {
		(SA, 0) : (1, MR, SB),
		(SA, 1) : (1, ML, SC),
		(SB, 0) : (1, ML, SA),
		(SB, 1) : (1, MR, SB),
		(SC, 0) : (1, ML, SB),
		(SC, 1) : (1, MR, SH)
}

class TM(CA):
	def __init__(self, n = 100):
		ratio = 2
		super(TM, self).__init__(000, n, ratio)
		self.state = SA
		self.head = self.m / 2

	def step(self):
		i = self.next
		symbol = self.array[i, self.head]
		if (self.state != SH):
			write, move, self.state = AT[(self.state, symbol)]
			self.array[i, self.head] = write
			if (i+1 < n):
				self.array[i+1] = self.array[i] # update "next" tape
			self.head = self.head - 1 if move == ML else self.head + 1
			self.next += 1

	def __str__(ca):
		out = ''
		for j in range(ca.m):
			out += '\033[1m' if  (j == ca.head) else ""
			out += '%2d' % ca.array[i, j]
			out += '\033[0m' if  (j == ca.head) else ""
			out += '|'
		out += '\n'
		return out

if __name__ == '__main__':
	n = 20
	ca = TM(n)
	for i in range(n):
		out = ''
		out += 'Before step %d (Head = %d, State = %s):\n' % (i, ca.head, ca.state)
		out += str(ca)
		ca.step()
		out += 'After step %d (Head = %d, State = %s):\n' % (i, ca.head, ca.state)
		out += str(ca)
		print out
		if (ca.state == SH):
			break
### chap 6, ex 04 END   ###
