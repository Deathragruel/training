import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	""" Tests for name_function.py """
	def test_first_last_name(self):
		""" Do names like 'Janis Joplin' work? """
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')
	def test_first_middle_last_name(self):
		""" Do names like 'Wolfang Amadeus Mozart' """
		formatted_name = get_formatted_name('wolfang', 'mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfang Amadeus Mozart')
if __name__ == '__main__':
	unittest.main()