import unittest
import cap 
class TestCap(unittest.TestCase):


	def test_one_word(self):
		text = 'python'
		result = cap.text_cap(text)
		self.assertEqual(result, 'Python')

	def test_multiple_words(self):
		text = 'life is great'
		result = cap.text_cap(text)
		self.assertEqual(result, 'Life Is Great')


if __name__ == '__main__':
	unittest.main()