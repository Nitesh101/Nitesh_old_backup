"""def char(str):
	dict = {}
	for i in str:
		keys = dict.keys()
		if i in keys:
			dict[i] += 1
		else:
			dict[i] = 1
	return dict
print(char('google.com'))
	if len(str) < 2:
		return ' '
	return str[0:2]+ str[-2:]
print(is_string('w3resource'))
def change_char(str):
	char= str[0]
	length = len(str)
	str = str.replace(char,'$')
	str = char + str[1:]

	return str
"""
val = raw_input("Enter a input: ")
for i in range(0,val):
	for j in range(0,i):
		print "*"
	print '\n'
