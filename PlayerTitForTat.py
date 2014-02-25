def move(history):
	mine, theirs = history
	ret = theirs[-1] if len(theirs) > 0 else 'C'
	return ret
