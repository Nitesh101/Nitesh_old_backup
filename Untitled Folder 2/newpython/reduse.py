#!/usr/bin/python
"""
def func(v1,v2):
	sum = v1+v2
	return sum
print func(100,120)
mylist = range(1,101,1)
result = reduce(func,mylist)
print result

mylist = range(1,10)
func = lambda v1,v2:v1 + v2,mylist
print func

mylist = range(1,101,1)
sumnums = reduce(func,mylist)
print sumnums
"
def maxvalfunc(v1,v2):
	res = v1>v2
	if(res == True):
		res = v1
	else:	
		res = v2
	return res
mylist = [27,48,11,30,103]
sumnums = reduce(maxvalfunc,mylist)
print sumnums
"""
 

mylist = [47,28,39,290]
maxval = reduce(lambda v1,v2:v1 if (v2<v1) else v2,mylist)
print maxval
"""
mylist = [47,28,39,290]
maxvalfunc = reduce(maxval,mylist)
print maxvalfunc
"""
#map and lambda
def prefix(word):
	res = '--'+word
	return res
varible = ['m','func','y0']
options = []
var_names_len = len(varible)
for index in range(var_names_len):
	item = varible[index]
	new_item = prefix(item)
	options.append(new_item)
print options


options = map(prefix,varible)
print options

options = map(lambda word:'__'+word,varible)
print options
