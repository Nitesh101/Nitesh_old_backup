import unittest
import os
print "Execute Test case_ID_120: IP--->Call Put from multiple clients"
val3 = os.system("python test1.py put 1")
print val3

class Testcase(unittest.Testcase):
	def test_put(self):
		self.assertEqual(val3,0)
if __name__=='__main__':
	unittest.main()
