def count_len(str1):
	d = {}
	for i in str1:
		keys =d.keys()
		if i in keys:
			d[i] += 1
		else:
			d[i] =1
	return d
print count_len('google.com')
