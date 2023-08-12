#!/usr/bin/env python3

"""Test Base Model"""
from datetime import datetime
import unittest
from models.base_model import BaseModel
from unittest import mock
from time import sleep


class Test_Class_BaseModel(unittest.TestCase):
    """Testing BaseModel class"""

    def test_BaseModel_instance(self):
        """
        Test BaseModel attributes
        """
        instance = BaseModel()
        self.assertEqual(type(instance), BaseModel)
        self.assertTrue(type(instance) == BaseModel)
        self.assertIs(type(instance), BaseModel)
        instance.name = "Younesse"
        instance.email = "ye@dyns.dev"
        instance.number = 90
        expectec_attrs_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str,
            "email": str,
            "number": int
        }
        dict_inst = instance.to_dict()
        expectec_attrs = [
            "id",
            "created_at",
            "updated_at",
            "name",
            "email",
            "number",
            "__class__"]
        self.assertCountEqual(dict_inst.keys(), expectec_attrs)
        self.assertEqual(dict_inst['name'], 'Younesse')
        self.assertEqual(dict_inst['email'], 'ye@dyns.dev')
        self.assertEqual(dict_inst['number'], 90)
        self.assertEqual(dict_inst['__class__'], 'BaseModel')

        for attr, types in expectec_attrs_types.items():
            with self.subTest(attr=attr, typ=types):
                self.assertIn(attr, instance.__dict__)
                self.assertIs(type(instance.__dict__[attr]), types)

    def test_datetime(self):
        """
        Test correct datetime assigned of created_at and updated_at
        """
        created_at = datetime.now()
        instance1 = BaseModel()
        updated_at = datetime.now()
        self.assertEqual(created_at <= instance1.created_at, True)
        self.assertEqual(instance1.created_at <= updated_at, True)
        sleep(1)
        created_at = datetime.now()
        instance2 = BaseModel()
        updated_at = datetime.now()
        self.assertEqual(created_at <= instance2.created_at, True)
        self.assertEqual(instance2.created_at <= updated_at, True)
        self.assertNotEqual(instance1.created_at, instance2.created_at)
        self.assertNotEqual(instance1.updated_at, instance2.updated_at)

    def test_uuid(self):
        """
        Testin UUID
        """
        instance1 = BaseModel()
        instance2 = BaseModel()
        instance3 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)
        self.assertNotEqual(instance1.id, instance3.id)
        self.assertNotEqual(instance2.id, instance3.id)

    def test_str_method(self):
        """Testing returns STR method"""
        instance6 = BaseModel()
        string_output = "[BaseModel] ({}) {}".format(instance6.id,
                                                     instance6.__dict__)
        self.assertEqual(string_output, str(instance6))

    def test_save_method(self):
        """Testing save method"""

        instance = BaseModel()
        created_ats = instance.created_at
        sleep(2)
        updated_ats = instance.updated_at
        instance.save()
        saved_inst = instance.created_at
        sleep(2)
        updated_inst = instance.updated_at
        self.assertNotEqual(updated_ats, updated_inst)
        self.assertEqual(created_ats, saved_inst)

        instance.save()
        bmid = "BaseModel." + instance.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


if __name__ == '__main__':
    unittest.main
