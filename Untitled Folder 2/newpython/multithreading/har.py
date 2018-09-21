val = input("please enter a values: ")
start,stop,step = 0,10,1
if isinstance(val,int):
	start = 0
	step = 1
	stop = val
elif len(val) == 2:
	start = val[0]
	stop = val[1]
elif len(val) == 3:
	start = val[0]
	stop = val[1]
	step = val[2]
else:
	start = 0
	stop = 10
	step = 1
if(start < stop):
	result = [val for val in range(start,stop,step) if val%2==0]
print result

