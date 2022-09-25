import unittest
from city_functions import get_location

class LocationTestCase(unittest.TestCase):
	def test_city_country(self):
		location = get_location('santiago', 'chile')
		self.assertEqual(location, 'Santiago, Chile')
	def test_city_country_population(self):
		location = get_location('karachi', 'pakistan', '11 million')
		self.assertEqual(location, 'Karachi, Pakistan- Population 11 Million')
if __name__ == '__main__':
	unittest.main()