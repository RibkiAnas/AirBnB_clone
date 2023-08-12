#!/usr/bin/python3
"""Place Model Unit tests"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test Plase Model"""

    def test_Place(self):
        """Test plase"""

        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)
        self.assertIsInstance(place.id, str)
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
