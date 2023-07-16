#!/usr/bin/python3
"""Tests for user.py module"""
import unittest
from models.user import User


class TestUserClass(unittest.TestCase):
    """Unittests for Class User"""
    def setUp(self):
        self.user = User()

    def tearDown(self):
        del self.user

    def test_instance_creation(self):
        """Test if an instance of User is correctly created"""
        self.assertIsInstance(self.user, User)

    def test_attributes(self):
        """Test the attributes of User"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_attributes_default_values(self):
        """Test the default values of attributes"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_to_dict_method(self):
        """Test the to_dict method of User"""
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertTrue('id' in user_dict)
        self.assertTrue('created_at' in user_dict)
        self.assertTrue('updated_at' in user_dict)

    def test_str_method(self):
        """Test the __str__ method of User"""
        user_str = str(self.user)
        expected_str = "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(user_str, expected_str)


if __name__ == '__main__':
    unittest.main()
