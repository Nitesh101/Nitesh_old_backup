import unittest
import os

val = os.system("python test1.py init 1 ")
val2 = os.system("python test1.py discover 1")
val3 = os.system("python test1.py put 1")
print val3

class Testcase(unittest.Testcase):
	def test_put(self):
		self.assertEqual(val3,0)
if __name__=='__main__':
	unittest.main()

