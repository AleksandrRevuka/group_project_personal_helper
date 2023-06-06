"""Tests validation"""

import unittest
from personal_helper.entities import User, Email, Phone
from personal_helper.address_book import AddressBook as AB, Record
from personal_helper.validation import (
    name_validation,
    phone_validation,
    email_validation,
    birthday_date_validation,
    criteria_validation,
    check_name_in_address_book,
    check_name_not_in_address_book,
    check_email_in_address_book,
    check_email_not_in_address_book,
    check_phone_number_in_address_book,
    check_phone_number_not_in_address_book
)


class TestValidation(unittest.TestCase):
    """Tests validation"""

    def test_validation_email_with_invalid_input(self) -> None:
        """
        The test_verify_email_with_invalid_input function tests the verify_email function with an invalid input.
        The test is successful if the SystemExit exception is raised and 'Try again!' is printed to stdout.
        """
        email = 'test@sasha@gmail.com'

        with self.assertRaises(SystemExit) as context:
            email_validation(email)
        self.assertEqual('Try again!', context.exception.code)

    def test_validation_email_with_valid_input(self) -> None:
        """
        The test_verify_email_with_valid_input function tests the verify_email function with a valid input.
            The expected output is None, and the actual output should be equal to the expected output.
        """
        email = "john.doe@example.com"
        expected_output = None

        actual_output = email_validation(email)

        self.assertEqual(actual_output, expected_output)

    def test_validation_phone_with_invalid_input(self) -> None:
        """
        The test_verify_phone_with_invalid_input function tests the verify_phone function in the Phone class.
        It checks that an error is raised if a phone number contains non-digits, or if it's too short or long.
        """
        phone = '+plus380951234567'
        with self.assertRaises(SystemExit) as context:
            phone_validation(phone)
        self.assertEqual('Try again!', context.exception.code)

        phone = '3809'
        with self.assertRaises(SystemExit) as context:
            phone_validation(phone)
        self.assertEqual('Try again!', context.exception.code)

        phone = '380951234567123456789'
        with self.assertRaises(SystemExit) as context:
            phone_validation(phone)
        self.assertEqual('Try again!', context.exception.code)

    def test_phone_validation_with_valid_input(self) -> None:
        """
        The test_phone_validation_with_valid_input function tests the phone_validation function with a valid input.
        The expected output is False, because the phone number is valid.
        """
        phone = "380631234567"

        actual_output = phone_validation(phone)

        self.assertFalse(actual_output, False)

    def test_validation_name_with_invalid_input(self) -> None:
        """
        The test_verify_name function tests the Name class's name property.
        The function raises a TypeError if the new_name variable is not a string, and raises a 
        ValueError if it is an empty string or longer than 50 characters.
        """
        name_invalid_num = 12
        with self.assertRaises(SystemExit) as context:
            name_validation(name_invalid_num)
        self.assertEqual('Try again!', context.exception.code)

        name = 'new_name'
        with self.assertRaises(SystemExit) as context:
            name_validation(name)
        self.assertEqual('Try again!', context.exception.code)

        name = ''
        with self.assertRaises(SystemExit) as context:
            name_validation(name)
        self.assertEqual('Try again!', context.exception.code)

        name = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        with self.assertRaises(SystemExit) as context:
            name_validation(name)
        self.assertEqual('Try again!', context.exception.code)

    def test_name_validation_with_valid_input(self) -> None:
        """
        The test_name_validation_with_valid_input function tests the name_validation function with a valid input.
        The expected output is False, and the actual output is also False.
        """
        name = "Alex"
        actual_output = name_validation(name)
        self.assertFalse(actual_output, False)

    def test_verify_birthday_date_with_invalid_input(self) -> None:
        """
        The test_verify_birthday_date_with_invalid_input function tests the verify_birthday_date function in the Birthday class.
        It checks that an error is raised if a date is not entered correctly, and also checks that an error is raised if a future date is entered.
        """
        birthday_date = '31-04-2000'
        with self.assertRaises(SystemExit) as context:
            birthday_date_validation(birthday_date)
        self.assertEqual('Try again!', context.exception.code)

        birthday_date = '30-04-2030'
        with self.assertRaises(SystemExit) as context:
            birthday_date_validation(birthday_date)
        self.assertEqual('Try again!', context.exception.code)

    def test_verify_criteria_with_invalid_input(self) -> None:
        """
        The test_verify_criteria_with_invalid_input function tests the verify_criteria function with invalid input.
                The test is successful if the SystemExit exception is raised and an error message is printed to stdout.
        """
        criteria = '_'
        with self.assertRaises(SystemExit) as context:
            criteria_validation(criteria)
        self.assertEqual('Try again!', context.exception.code)

    def test_check_name_in_address_book(self) -> None:
        """
        The test_check_name_in_address_book function checks if the name is already in the address book.
        If it is, then a message will be returned to inform that this contact already exists.
        """
        address_book = AB()
        contact = Record(User("Alex"))
        address_book.add_record(contact)
        name = "Alex"

        with self.assertRaises(SystemExit) as context:
            check_name_in_address_book(address_book, name)
        self.assertEqual('Try again!', context.exception.code)

    def test_check_name_not_in_address_book(self) -> None:
        """
        The test_check_name_not_in_address_book function checks that the name is not in the address book.
            If it is, then an error message will be returned.
        """
        address_book = AB()
        contact = Record(User("Alex"))
        address_book.add_record(contact)
        name = "Olya"

        with self.assertRaises(SystemExit) as context:
            check_name_not_in_address_book(address_book, name)
        self.assertEqual('Try again!', context.exception.code)

    def test_check_phone_number_in_address_book(self) -> None:
        """
        The test_check_phone_number_in_address_book function checks if the phone number is already in the address book.
        If it is, then an exception will be raised and a message will appear on the screen.
        """
        address_book = AB()
        name = "Alex"
        phone_test = Phone('3809991112233')
        contact = Record(User(name))
        contact.add_phone_number(phone_test)
        phone = Phone('3809991112233')
        address_book.add_record(contact)

        with self.assertRaises(SystemExit) as context:
            check_phone_number_in_address_book(contact, phone, name)
        self.assertEqual('Try again!', context.exception.code)

    def test_check_phone_number_not_in_address_book(self) -> None:
        """
        The test_check_phone_number_not_in_address_book function checks if the phone number is already in the address book.
        If it is, then an error message will be displayed and the user will have to enter a new phone number.
        """

        address_book = AB()
        name = "Alex"
        phone_test = Phone('3809991112233')
        contact = Record(User(name))
        contact.add_phone_number(phone_test)
        phone = Phone('3809998887766')
        address_book.add_record(contact)

        with self.assertRaises(SystemExit) as context:
            check_phone_number_not_in_address_book(contact, phone, name)
        self.assertEqual('Try again!', context.exception.code)

    def test_check_email_in_address_book(self) -> None:
        """
        The test_check_email_in_address_book function checks if the email is already in the address book.
        If it is, then an error message will be displayed and the user will have to try again.
        """
        address_book = AB()
        contact = Record(User("Alex"))
        email_test = Email('test_sasha@gmail.com')
        contact.add_email(email_test)
        email = Email('test_sasha@gmail.com')
        address_book.add_record(contact)
        name = "Alex"

        with self.assertRaises(SystemExit) as context:
            check_email_in_address_book(contact, email, name)
        self.assertEqual('Try again!', context.exception.code)

    def test_check_email_not_in_address_book(self) -> None:
        """
        The test_check_email_not_in_address_book function checks if the email is already in the address book.
        If it is, then an error message will be printed and the user will be asked to try again.
        """
        address_book = AB()
        contact = Record(User("Alex"))
        email_test = Email('test_sasha@gmail.com')
        contact.add_email(email_test)
        email = Email('sasha@gmail.com')
        address_book.add_record(contact)
        name = "Alex"

        with self.assertRaises(SystemExit) as context:
            check_email_not_in_address_book(contact, email, name)
        self.assertEqual('Try again!', context.exception.code)


if __name__ == '__main__':
    unittest.main()
