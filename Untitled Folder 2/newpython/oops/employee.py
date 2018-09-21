#!/usr/bin/python
class Employee:
	'comman base calss for all employee'
	empcount = 0
	def __init__(self,ename,eid):
		self.ename = ename
		self.eid = eid
		Employee.empcount +=1
		return
	def displayCount(self):
		print "Total Employee %d"%(Employee.empcount)
		return
	def displayEmployee(self):
		print "Employee Name:",self.ename
		print "Employee ID:",self.eid
		return
emp1 = Employee("nitesh",101)
emp2 = Employee("harshitha",102)
emp1.displayEmployee()
emp2.displayEmployee()
emp1.displayCount()
print "Total Employee(accessing class variable):%d"%Employee.empcount


emp1.location = "Banjara Hills"
print "Employee 3 Location(current):",emp1.location
emp2.location = "Gachibowli"
print "Emplooyee 3 Location(New):",emp2.location
del emp1.location
res = hasattr(emp2,'location')
print res
loc = getattr(emp2,'location')
print loc




print "Employee.__doc__:",Employee.__doc__
print "Employee.__name__:",Employee.__name__
print "Employee.__module__:",Employee.__module__
print "Employee.__bases__:",Employee.__bases__
print "Employee.__dict__:",Employee.__dict__
