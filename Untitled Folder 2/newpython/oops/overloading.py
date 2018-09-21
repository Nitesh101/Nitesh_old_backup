#!/usr/bin/python
class Vector:
	def __init__(self,num1,num2):
		self.num1=num1
		self.num2=num2
	def __str__(self):
		return 'Vector(%d,%d)'%(self.num1,self.num2)
	def __add__(self,other):
		res = Vector(self.num1 + other.num1,self.num2 + other.num2)
		return res
	def __mul__(self,other):
		res = Vector(self.num1 * other.num1,self.num2 * other.num2)
		return res
	def __sub__(self,other):
		res = Vector(self.num1 - other.num1,self.num2 - other.num2)
		return res
v1 = Vector(2,10)
v2 = Vector(5,-2)
resadd=v1+v2
print resadd
resmul = v1 * v2
print resmul
ressub = v1 -v2
print ressub

	
