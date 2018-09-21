import unittest
import os
print ("Execute Test case_ID_30----> Call Put once to secure connection by Authorized client.")
#val = os.system("python run.py init 1")
#val = os.system("python run.py discover 1")
val = os.system("python run.py init 1 discover 1  get 1 put 2 ")
print val
class TestCase(unittest.TestCase):
	def test_put(self):
		self.assertEqual(val,0)
if __name__=='__main__':
	unittest.main()
