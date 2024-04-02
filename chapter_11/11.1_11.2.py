# 11.1 City, country
# city_functions
def city_country(city, country):
    """generated name of city and country"""
    full_name = f"{city.title()}, {country.title()}"
    return full_name.title()

# test_cities
import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    """Return a text with city and country"""
    def test_city_country(self):
        formatted_name = city_country('oslo', 'norway')
        self.assertEqual(formatted_name, 'Oslo, Norway')

if __name__ == '__main__':
    unittest.main()

# 11.2 Population
# city_functions
def city_country(city, country, population = 0):
    """generated name of city and country - population"""
    full_name = f"{city.title()}, {country.title()}"
    if population:
        full_name += f" - population {population}"
    return full_name

# test cities
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

