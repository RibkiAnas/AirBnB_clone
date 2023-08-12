#!/usr/bin/python3
"""State Model Unit tests"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test State Model"""

    def test_State(self):
        """Test State"""
        state = State()

        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)
        self.assertIsInstance(state.id, str)
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
