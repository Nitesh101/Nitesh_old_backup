import unittest
import os
print ("Execute Test case_ID_47---->Call Put repeatedly  for same resource")
val = os.system("python run.py init 1 discover 1 put 1")
print val
class TestCase(unittest.TestCase):
	def test_put(self):
		self.assertEqual(val,0)
if __name__=='__main__':
	unittest.main()