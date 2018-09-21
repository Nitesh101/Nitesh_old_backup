import ctypes
import unittest
class FooLibTestCase(unittest.TestCase):
	def setUp(self):
		self.cprogram = ctypes.CDLL('/home/madisnit/Desktop/cprogram.c')
	def test_01a(self):
		self.failUnlessEqual(4,cprogram.my_sum(2,2))
if __name__ == '__main__': 
    unittest.main()


