str1=input("enter a string")
sub_str=input("enter the sub string")
if (sub_str in str1):
	print sub_str ,"is a substring of",str1
elif (sub_str not in str1):
	print sub_str,"is not a substring",str1
