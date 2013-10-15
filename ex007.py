import string

def gen_identifier():
	i = 1
	while (True):
		for c in string.lowercase:
			yield "%s%s" % (c, i)
		i += 1

def main(script, *args):
	iter = gen_identifier()
	for n in range(100):
		print iter.next()



if __name__ == '__main__':
	import sys
	main(*sys.argv)
