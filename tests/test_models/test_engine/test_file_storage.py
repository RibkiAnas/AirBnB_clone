#!/usr/bin/python3
"""File Storage Testing"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test normal base instantiation"""

    def test_file_storage(self):
        """Test FileStorage"""
        fs = FileStorage()
        base = BaseModel()

        fs.new(base)

        self.assertIsInstance(fs, FileStorage)
        self.assertIsInstance(fs.all(), dict)
        self.assertIn("{}.{}".format("BaseModel", base.id), fs.all())


if __name__ == '__main__':
    unittest.main()
