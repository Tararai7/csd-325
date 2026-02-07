"""
test_cities.py
CSD-325 Module 7 Assignment
Student: Tara Rai
Date: 02/07/2026

Unit tests for the city_country function using Python's unittest framework.
"""

import unittest
from city_functions import city_country


class TestCityCountry(unittest.TestCase):
    """Test cases for the city_country function."""
    
    def test_city_country(self):
        """Test the basic city, country format without optional parameters."""
        result = city_country("santiago", "chile")
        self.assertEqual(result, "Santiago, Chile")
    
    def test_city_country_population(self):
        """Test city, country format with population parameter."""
        result = city_country("santiago", "chile", population=5000000)
        self.assertEqual(result, "Santiago, Chile - population 5,000,000")
    
    def test_city_country_population_language(self):
        """Test city, country format with both population and language parameters."""
        result = city_country("santiago", "chile", population=5000000, language="spanish")
        self.assertEqual(result, "Santiago, Chile - population 5,000,000, Spanish")


if __name__ == "__main__":
    unittest.main()