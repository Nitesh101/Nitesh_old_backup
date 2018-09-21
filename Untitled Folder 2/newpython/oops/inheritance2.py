#!/usr/bin/python
class SchoolMember:
	def __init__(self,name,age):
		self.name = name
		self.age = age
		print "Initialized school member:",(self.name)
	def tell(self):
		print 'Name:"{}" Age:"{}"',(self.name, self.age)
class Teacher(SchoolMember):
	def __init__(self, name, age,salary):
		SchoolMember.__init__(self,name,age)
		self.salary = salary
		print('initialized Teacher:{}'),format(self.name)
	def tell(self):
		SchoolMember.tell(self)
		print 'salary:"{:d}"',(self.salary)
class Student(SchoolMember):
	def __init__(self,name,age,marks):
		SchoolMember.__init__(self,name,age)
		self.marks = marks
		print ('initialized student:{}'),(self.name)
	def tell(self):
		SchoolMember.tell(self)
		print 'Marks:"{:d}"',(self.marks)
t  = Teacher('Mrs.shrividya',40,30000)
s = Student('srujan',25,75)
members = [t,s]
for member in members:
	member.tell()
