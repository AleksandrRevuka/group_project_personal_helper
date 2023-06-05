"""Tests class Phone"""
import unittest

from personal_helper.utils import sanitize_phone_number
from personal_helper.entities import Phone


class TestPhone(unittest.TestCase):
    """Tests class Phone"""

    def setUp(self) -> None:
        self.phone_test = Phone('380951234567')
        self.phone_test_none = Phone()

    def tearDown(self) -> None:
        del self.phone_test

    def test_set_phone_valid(self) -> None:
        """
        The test_set_phone function tests the set_phone function of the Phone class.
        It checks if a phone number is correctly formatted and stored in an instance of
        the Phone class.
        """
        self.assertEqual(self.phone_test.phone, '380951234567')

    def test_set_phone_none(self) -> None:
        """
        The test_set_phone_none function tests the set_phone function in the Phone class.
        The test_set_phone_none function is a unit test that checks to see if the phone number
        is None when it is not given any input.
        """
        self.assertEqual(self.phone_test_none.phone, None)

    def test_eq_phones(self) -> None:
        """The test_eq_phones function tests the equality of two phone numbers."""
        phone_test = Phone('380951234567')
        self.assertEqual(phone_test, self.phone_test)
        
        phone_test_invalid = '380951234567'
        self.assertNotEqual(phone_test_invalid, self.phone_test)

    def test_sanitize_phone_number(self) -> None:
        """
        The test_sanitize_phone_number function tests the sanitize_phone_number function in Phone.py
        It takes a phone number as an argument and returns it with all non-numeric characters removed.
        """

        phone_test = sanitize_phone_number('38(095)123-45-67')
        self.assertEqual(phone_test, '+380951234567')


if __name__ == '__main__':
    unittest.main()