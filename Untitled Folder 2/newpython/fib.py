def recr_fibo(n):
	"""recursive function"""
	if n <= 1:
		return n
	else:
		return(recr_fibo(n-1) + recr_fibo(n-2))
nterms = 10
if nterms <  0:
	print ("please enter a positive integer : ")
else:
	print ("fibonacci sequence : ")
	for i in range(nterms):
		print (recr_fibo(i))
