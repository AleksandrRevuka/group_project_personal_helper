"""Tests validation"""

import unittest
from personal_helper.validation import (
    verify_email,
    verify_phone,
    verify_name,
    verify_birthday_date,
    verify_criteria,
)


class TestValidation(unittest.TestCase):
    """Tests validation"""

    # def setUp(self) -> None:
    # self.email_test = Email('test_sasha@gmail.com')

    # def tearDown(self) -> None:
    # del self.email_test

    def test_verify_email_with_invalid_input(self):
        """
        The test_verify_email_with_invalid_input function tests the verify_email function with an invalid input.
        The test is successful if the SystemExit exception is raised and 'Try again!' is printed to stdout.
        """
        email = 'test@sasha@gmail.com'

        with self.assertRaises(SystemExit) as context:
            verify_email(email)
        self.assertEqual('Try again!', context.exception.code)

    def test_verify_email_with_valid_input(self):
        """
        The test_verify_email_with_valid_input function tests the verify_email function with a valid input.
            The expected output is None, and the actual output should be equal to the expected output.
        """
        email = "john.doe@example.com"
        expected_output = None

        actual_output = verify_email(email)

        self.assertEqual(actual_output, expected_output)

    def test_verify_phone_with_invalid_input(self):
        """
        The test_verify_phone_with_invalid_input function tests the verify_phone function in the Phone class.
        It checks that an error is raised if a phone number contains non-digits, or if it's too short or long.
        """
        phone = '+plus380951234567'
        with self.assertRaises(SystemExit) as context:
            verify_phone(phone)
        self.assertEqual('Try again!', context.exception.code)

        phone = '3809'
        with self.assertRaises(SystemExit) as context:
            verify_phone(phone)
        self.assertEqual('Try again!', context.exception.code)

        phone = '380951234567123456789'
        with self.assertRaises(SystemExit) as context:
            verify_email(phone)
        self.assertEqual('Try again!', context.exception.code)

    def test_verify_name_with_invalid_input(self):
        """
        The test_verify_name function tests the Name class's name property.
        The function raises a TypeError if the new_name variable is not a string, and raises a 
        ValueError if it is an empty string or longer than 50 characters.
        """
        name = 12
        with self.assertRaises(SystemExit) as context:
            verify_name(name)
        self.assertEqual('Try again!', context.exception.code)

        name = 'new_name'
        with self.assertRaises(SystemExit) as context:
            verify_name(name)
        self.assertEqual('Try again!', context.exception.code)

        name = ''
        with self.assertRaises(SystemExit) as context:
            verify_name(name)
        self.assertEqual('Try again!', context.exception.code)

        name = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        with self.assertRaises(SystemExit) as context:
            verify_name(name)
        self.assertEqual('Try again!', context.exception.code)

    def test_verify_birthday_date_with_invalid_input(self):
        """
        The test_verify_birthday_date_with_invalid_input function tests the verify_birthday_date function in the Birthday class.
        It checks that an error is raised if a date is not entered correctly, and also checks that an error is raised if a future date is entered.
        """
        birthday_date = '31-04-2000'
        with self.assertRaises(SystemExit) as context:
            verify_birthday_date(birthday_date)
        self.assertEqual('Try again!', context.exception.code)

        birthday_date = '30-04-2030'
        with self.assertRaises(SystemExit) as context:
            verify_birthday_date(birthday_date)
        self.assertEqual('Try again!', context.exception.code)

    def test_verify_criteria_with_invalid_input(self):
        """
        The test_verify_criteria_with_invalid_input function tests the verify_criteria function with invalid input.
                The test is successful if the SystemExit exception is raised and an error message is printed to stdout.
        """
        criteria = '_'
        with self.assertRaises(SystemExit) as context:
            verify_criteria(criteria)
        self.assertEqual('Try again!', context.exception.code)


if __name__ == '__main__':
    unittest.main()
