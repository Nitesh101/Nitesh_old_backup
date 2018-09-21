"""
count = 0
while True:
	print(count)
	count += 1
	if count >= 5:
		break


for x in range(10):
	if x % 2 == 0:
		continue
	print(x)

for i in range(1,10):
	if(i%5==0):
		break
	print(i)
else:
	print "this is not printed"

for letter in 'python':
	print "Current Letter : ",letter
"""
fruit = ['banana','apple','mango']
for index in fruit:
	print index
