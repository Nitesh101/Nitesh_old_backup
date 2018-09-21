#!/usr/bin/python
from random import randrange

def random_list():
	"please list"
	result = []
	count = randrange(6,40)

#        count = randrange(1,10)

	#count = randrange(1,10)
	for index in range(count):
		result+=[randrange(-50,50)]
	return result

def sel_sort(res):
	print res
	count=len(res)
	for index1 in range(count-1):
		small=index1
		for index2 in range(index1+1,count):
			if res[index2]<res[small]:
				small=index2
		if index1 !=small:
			res[index1],res[small]=res[small],res[index1]
			
	print res
	return

lis1=random_list()
sel_sort(lis1)




