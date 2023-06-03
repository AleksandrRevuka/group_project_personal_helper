"""Tests class Phone"""
import unittest

from personal_helper.utils import sanitize_phone_number
from personal_helper.entities import Phone


class TestPhone(unittest.TestCase):
    """Tests class Phone"""

    def setUp(self) -> None:
        self.phone_test = Phone('380951234567')

    def tearDown(self) -> None:
        del self.phone_test

    def test_phone(self):
        """The test_phone function tests the phone number of a person."""

        self.assertEqual(self.phone_test.phone, '380951234567')

    def test_set_phone(self):
        """
        The test_set_phone function tests the set_phone function of the Phone class.
        It checks if a phone number is correctly formatted and stored in an instance of
        the Phone class.
        """

        self.phone_test.phone = '380989876543'
        self.assertEqual(self.phone_test.phone, '380989876543')

    def test_eq_phones(self):
        """The test_eq_phones function tests the equality of two phone numbers."""

        phone_test = Phone('380951234567')
        self.assertEqual(phone_test, self.phone_test)

    def test_sanitize_phone_number(self):
        """
        The test_sanitize_phone_number function tests the sanitize_phone_number function in Phone.py
        It takes a phone number as an argument and returns it with all non-numeric characters removed.
        """

        phone_test = sanitize_phone_number('38(095)123-45-67')
        self.assertEqual(phone_test, '+380951234567')


if __name__ == '__main__':
    unittest.main()