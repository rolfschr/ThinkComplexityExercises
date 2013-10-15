
l = range(100)


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


def main(script, t, *args):
	print l
	t = int(t)
	print bisect(t, l)



if __name__ == '__main__':
	import sys
	main(*sys.argv)
