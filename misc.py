import string

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

def main(script, *args):
	iter = gen_identifier()
	for n in range(100):
		print iter.next()



if __name__ == '__main__':
	import sys
	main(*sys.argv)
