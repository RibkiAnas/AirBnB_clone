#!/usr/bin/python3
"""BaseModel Unittests"""


import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """test BaseModel"""

    def test_base(self):
        """test create BaseModel"""

        base = BaseModel()

        self.assertIsInstance(base, BaseModel)
        self.assertIsInstance(base.id, str)

    def test_kwargs(self):
        """test BaseModel with dictionary"""

        test_d = {"updated_at": "2023-08-09T14:20:16.087199",
                  "created_at": "2023-08-09T14:20:16.087199",
                  "id": "1d7cb90a-5cbe-41fe-89c6-6694442b9350",
                  "__class__": "BaseModel"}
        base = BaseModel(**test_d)
        str_test = "[{}] ({}) {}".format(test_d["__class__"], test_d["id"],
                                         base.__dict__)

        self.assertIsInstance(base, BaseModel)
        self.assertEqual(base.id, "1d7cb90a-5cbe-41fe-89c6-6694442b9350")
        self.assertIsInstance(base.updated_at, datetime)
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.to_dict(), dict)
        self.assertEqual(base.__str__(), str_test)

    def test_base_save(self):
        """test BaseModel.save"""

        base = BaseModel()
        base.save()
        self.assertNotEqual(base.created_at, base.updated_at)


if __name__ == '__main__':
    unittest.main()
