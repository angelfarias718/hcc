import unittest

from hcodechallenge import answer

class ConRunTest(unittest.TestCase):

	def test_consnumber(self):
		a=[1,2,3,5,10,9,8,9,10,11,7]
		self.assertTrue(
			[0,4,6,7],
			answer()
			)

if __name__=='__main__':
	unittest.main()
