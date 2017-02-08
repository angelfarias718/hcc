import unittest

from hcodechallenge import consec

class ConRunTest(unittest.TestCase):

	def test_consnumber(self):
		a=[1,2,3,5,10,9,8,9,10,11,7]
		self.assertEqual(
			[0,4,6,7],
			consec(a)
			)

if __name__=='__main__':
	unittest.main()
