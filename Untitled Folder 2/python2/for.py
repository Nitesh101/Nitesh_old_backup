"""
num = input("Enter a number: ")
if num > 1:
	for i in range(2,num):
		if (num%i) == 0:
			print num,"is not prime number"
			break
	else:
		print num,"is prime number"
"""
def fibanacci(n):
	a,b,counter = 0,1,0
	while True:
		if (counter > n ): return
		yield a
		a,b = b,a+b
		counter += 1
f = fibanacci(5)
for i in f:
	print i
