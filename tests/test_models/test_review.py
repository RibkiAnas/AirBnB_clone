#!/usr/bin/python3
"""Review Model Unit tests"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test Review Model"""

    def test_Review(self):
        """Test review"""
        review = Review()

        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)
        self.assertIsInstance(review.id, str)
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
