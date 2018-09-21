import unittest
import os
print "Execute Test case_ID_24: Call Put once to non secure connection"
print val3

class Testcase(unittest.Testcase):
	def test_put(self):
		self.assertEqual(val3,0)
if __name__=='__main__':
	unittest.main()

