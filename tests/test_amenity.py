#!/usr/bin/python3
"""Amenity Model Unittests"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test Amenity Model"""

    def test_Amenity(self):
        """test amenity"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)
        self.assertIsInstance(amenity.id, str)
        self.assertEqual(Amenity.name, "")


if __name__ == '__main__':
    unittest.main()
