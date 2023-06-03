"""Tests class Email"""
import unittest
from personal_helper.entities import Email


class TestEmail(unittest.TestCase):
    """Tests class Email"""

    def setUp(self) -> None:
        self.email_test = Email('test_sasha@gmail.com')

    def tearDown(self) -> None:
        del self.email_test

    def test_set_email(self):
        """
        The test_set_email function tests the set_email function in the Email class.
        It checks to see if an email address is properly assigned to a new instance of
        the Email class.
        """
        self.assertEqual(self.email_test.email, 'test_sasha@gmail.com')

if __name__ == '__main__':
    unittest.main()