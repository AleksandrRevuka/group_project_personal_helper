"""Tests class Email"""
import unittest
from personal_helper.entities import Email


class TestEmail(unittest.TestCase):
    """Tests class Email"""

    def setUp(self) -> None:
        self.email_test = Email('test_sasha@gmail.com')
        self.email_test_second = Email('test_sasha@gmail.com')
        self.email_test_none = Email()
        self.non_email = 'test_sasha@gmail.com'

    def tearDown(self) -> None:
        del self.email_test

    def test_set_email_valid(self) -> None:
        """
        The test_set_email function tests the set_email function in the Email class.
        It checks to see if an email address is properly assigned to a new instance of
        the Email class.
        """
        self.assertEqual(self.email_test.email, 'test_sasha@gmail.com')

    def test_set_email_none(self) -> None:
        """
        The test_set_email_none function tests the set_email function with a None value.
        The expected result is that the email attribute of an instance of Email will be set to None.
        """
        self.assertEqual(self.email_test_none.email, None)

    def test_equal_emails(self) -> None:
        """
        The test_equal_emails function tests the equality of two email objects.
        The first test checks if the emails are equal, and the second test checks if they are not equal.
        """
        self.assertEqual(self.email_test, self.email_test_second)
        self.assertNotEqual(self.email_test, self.email_test_none)
        self.assertNotEqual(self.email_test, self.non_email)

if __name__ == '__main__':
    unittest.main()