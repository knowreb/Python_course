import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_name = city_country('oslo', 'norway')
        self.assertEqual(formatted_name, 'Oslo, Norway')

    def test_city_country__population(self):
        formatted_name = city_country('oslo', 'norway', 1000000)
        self.assertEqual(formatted_name, 'Oslo, Norway - population 1000000')

if __name__ == '__main__':
    unittest.main()