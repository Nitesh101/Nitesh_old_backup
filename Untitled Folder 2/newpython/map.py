#!/usr/bin/python
"""
def calculatesquare(num):
	sqr = num*num
	return sqr
print calculatesquare(5)


numbers = (1,2,3,4)
result = map(calculatesquare,numbers)
print(result)

numberssquare = set(result)
print(numberssquare)



number = [1,2,3,4]
result = map(lambda num:num**2,number)
print result


words = 'The quick brown fox jumps over the lazy dog'
stuff = map(lambda word: [word.upper(),word.lower(),len(word)],words)
#print stuff

for word in words:
	print words

"""
l1 = [1,2,3,4]
l2 = [17,12,11,10]
l3 = [-1,-4,5,9]
sumlists = map(lambda v1,v2:v1+v2,l1,l2)
print sumlists


sumlists = map(lambda v1,v2,v3:v1+v2+v3,l1,l2,l3)
print sumlists


sumlists = map(lambda v1,v2,v3:v1+v2-v3,l1,l2,l3)
print sumlists

