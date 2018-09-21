import unittest
import os
print ("Execute Test case_ID_164---->Call Put with wrong input data")
val = os.system("python run.py put 1")
print val
class TestCase(unittest.TestCase):
	def test_put(self):
		self.assertEqual(val,0)
if __name__=='__main__':
	unittest.main()
