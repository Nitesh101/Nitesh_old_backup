#!/usr/bin/python

exp= "123*+"

def eval_postfix(exp):
    tmplst = []
    res = None
    for eachitem in exp:
		if eachitem.isdigit():
			tmplst.append(int(eachitem))
		elif eachitem== "+":
			res= tmplst.pop() + tmplst.pop()
		elif eachitem== "-":
			res= tmplst.pop() - tmplst.pop()
		elif eachitem== "*":
			res= tmplst.pop() * tmplst.pop()
		elif eachitem== "/":
			res= tmplst.pop() / tmplst.pop()
		elif eachitem== "%":
			res= tmplst.pop() % tmplst.pop()
	
		if res is not None:
			tmplst.append(res)
    return tmplst.pop()


res= eval_postfix(exp)
print "result of "+exp+ " is",res
