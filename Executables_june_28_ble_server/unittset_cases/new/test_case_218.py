import unittest
import os
print ("Execute Test case_ID_218----> Call init after Put with non secure connection")
val = os.system("python run.py put 1")
print val
class TestCase(unittest.TestCase):
	def test_put(self):
		self.assertEqual(val,0)
if __name__=='__main__':
	unittest.main()