def fact(n):
	result = reduce(lambda x,y:x*y,range(1,n+1))
	yield result
b = fact(5)
print b.next()
