import unittest
import os
val3 = os.system('python test_case.py')
print val3
class TestCase(unittest.TestCase):
	def count_len(self):
		self.assertEqual(val3,0)
if __name__=="__main__":
	unittest.main()
