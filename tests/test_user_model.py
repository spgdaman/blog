import unittest
from app.models import User
from app import db

class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User(firstname = 'Simon', lastname='Waigi',
        username='SPG', email='simonwaigi@outlook.com', pass_hash='W3w3n!kunguni')
        self.assertTrue(u.pass_hash is not None)

    def test_no_password_getter(self):
        u = User(pass_hash='W3w3n!kunguni')
        with self.assertRaises(AttributeError):
            u.password
    
    def test_password_verification(self):
        u = User(pass_hash='W3w3n!kunguni')
        self.assertTrue(u.verify_password('W3w3n!kunguni'))
        self.assertFalse(u.verify_password('dog'))