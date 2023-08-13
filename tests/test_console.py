#!/usr/bin/python3
"""A unit test module for the console."""
import unittest
from unittest.mock import patch, Mock, MagicMock
from io import StringIO
from console import HBNBCommand
from models import storage


class TestHBNBCommand(unittest.TestCase):
    """Represents the test class for the HBNBCommand class."""

    def setUp(self):
        """Create an instance of HBNBCommand before each test"""
        self.console = HBNBCommand()

    def tearDown(self):
        """clean up after each test"""
        pass

    def test_create(self):
        """Test case for the create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create invalid_class")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.assertIsNotNone(obj_id)

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create City name='Marrakech'")
            obj_id = f.getvalue().strip()
            self.assertIsNotNone(obj_id)

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertIn('City.{}'.format(obj_id), storage.all().keys())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show City {}".format(obj_id))

        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            testKey = "BaseModel.{}".format(f.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create User")
            testKey = "User.{}".format(f.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create State")
            testKey = "State.{}".format(f.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create City")
            testKey = "City.{}".format(f.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create Amenity")
            testKey = "Amenity.{}".format(f.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create Place")
            testKey = "Place.{}".format(f.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create Review")
            testKey = "Review.{}".format(f.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())

    def test_show(self):
        """Test case for the show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show invalid_class")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel 551af")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show BaseModel {obj_id}")
            self.assertIn(obj_id, f.getvalue())

    def test_destroy(self):
        """Test case for the destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy invalid_class")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            obj = storage.all()["BaseModel.{}".format(obj_id)]

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"destroy BaseModel {obj_id}")
            self.assertEqual(f.getvalue().strip(), "")
            self.assertNotIn(obj, storage.all())

    def test_all(self):
        """Test case for the all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all invalid_class")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            self.assertNotEqual(f.getvalue().strip(), "")

    def test_update(self):
        """Test case for the update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update invalid_class")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {obj_id}")
            self.assertEqual(f.getvalue().strip(),
                             "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {obj_id} my_attr")
            self.assertEqual(f.getvalue().strip(), "** value missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {obj_id} my_attr 'value'")
            self.assertEqual(f.getvalue().strip(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            dict_ = {"name": "ye", "number": 5}
            self.console.onecmd(f"update BaseModel {obj_id} {dict_}")
            self.assertEqual(f.getvalue().strip(), "")

    def test_default(self):
        """Test case for the default command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("unknown_command")
            self.assertEqual(f.getvalue().strip(), "")

    def test_count(self):
        """Test case for the count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count BaseModel")
            self.assertNotEqual(f.getvalue().strip(), "")

    def test_quit(self):
        """Test case for the quit command"""
        self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Test case for the EOF command"""
        self.assertTrue(self.console.onecmd("EOF"))


if __name__ == '__main__':
    unittest.main()
