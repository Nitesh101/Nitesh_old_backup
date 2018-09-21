#!/usr/bin/python
def reverse(data):
	datalen = len(data)-1
	for index in range(datalen,-1,-1):
		yield data[index]
for char in reverse('golf'):
	print(char)
