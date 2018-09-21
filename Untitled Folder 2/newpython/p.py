number = 2
count = input("Enter number: ")
result = 1
while number:
#	result = reduce(lambda x,y: x*y, range(1,number+1))
	for val in range(1, number+1):
		result *= val
	if str(result)[-count:] == '0'*count:
		print number
		print result
		break
	number +=1
	result = 1 
