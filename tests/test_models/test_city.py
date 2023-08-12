#!/usr/bin/python3
"""City Model Unittests"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test City Model"""

    def test_City(self):
        """test city"""
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)
        self.assertIsInstance(city.id, str)
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
