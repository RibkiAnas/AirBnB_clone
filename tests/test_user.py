#!/usr/bin/python3
"""User Model Unit tests"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test User Model"""

    def test_user(self):
        """Test User"""
        user = User()

        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)
        self.assertIsInstance(user.id, str)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
