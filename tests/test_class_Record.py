"""Test class Record"""

import unittest
from datetime import date, datetime

from personal_helper.entities import Phone, User, Email
from personal_helper.address_book import Record


class TestRecord(unittest.TestCase):
    """Tests class Record"""

    def setUp(self) -> None:
        self.user_test = User('Sasha')
        self.phone_test = Phone('380951234567')
        self.email_test = Email('test_sasha@gmail.com')
        self.record_test = Record(self.user_test)
        self.record_test.add_phone_number(self.phone_test)
        self.record_test.add_email(self.email_test)

    def tearDown(self) -> None:
        del self.record_test
        del self.user_test
        del self.phone_test
        del self.email_test

    def test_add_phone_number(self) -> None:
        """
        The test_add_phone_number function tests the add_phone_number function of the Record class.
        It creates a phone object and adds it to a record object, then checks if that phone number is in the list of 
        numbers for that record.
        """

        self.assertEqual(self.record_test.phone_numbers[0].subrecord, Phone('380951234567'))

    def test_change_phone_number(self) -> None:
        """
        The test_edit_phone_number function tests the edit_phone_number method of the Record class.
        It creates a new record, adds an old phone number to it and then edits this phone number with a new one.
        The test checks if the list of phone numbers in this record contains only one element - our new phone number.
        """
        new_phone = Phone('380951234500')
        self.record_test.change_phone_number(self.phone_test, new_phone)
        self.assertEqual(self.record_test.phone_numbers[0].subrecord, new_phone)

    def test_delete_phone_number(self) -> None:
        """
        The test_delete_phone_number function tests the delete_phone_number method of the Record class.
        It creates a phone number object and adds it to a record, then deletes it from that record.
        The test passes if the list of phone numbers in that record is empty.
        """
        self.record_test.delete_phone_number(self.phone_test)
        self.assertEqual(self.record_test.phone_numbers, [])

    def test_add_email(self) -> None:
        """
        The test_add_email function tests the add_email function in Record.py
            The test_add_email function takes a self parameter, which is an instance of the TestRecord class.
            The assertEquals method compares two values and returns True if they are equal, or False otherwise.
        """
        self.assertEqual(self.record_test.emails[0].subrecord, Email('test_sasha@gmail.com'))

    def test_change_email(self) -> None:
        """
        The test_edit_email function tests the edit_email function in Record.py
            It creates a new email object and then calls the edit_email function on it, passing in
            an old email object and a new one. The test checks to see if the subrecord of emails[0] is equal to 
            our newly created email.
        """

        new_email = Email('test_pasha@gmail.com')
        self.record_test.change_email(self.email_test, new_email)
        self.assertEqual(self.record_test.emails[0].subrecord, new_email)

    def test_delete_email(self) -> None:
        """
        The test_delete_email function tests the delete_email function in Record.py
            The test_delete_email function takes a self parameter and an email parameter.
            The test_delete_email function calls the delete email method on record with the given email as a parameter.
            Then, it asserts that there are no emails left in record.
        """

        self.record_test.delete_email(self.email_test)
        self.assertEqual(self.record_test.emails, [])

    def test_add_birthday(self) -> None:
        """
        The test_add_birthday function tests the add_birthday function in the Record class.
        It takes a date object as an argument and adds it to the birthday attribute of a record instance.
        """
        self.record_test.add_birthday('26-06-1982')
        self.assertEqual(self.record_test.user.birthday_date, date(1982, 6, 26))

    # def test_days_to_birthday(self) -> None:
    #     """
    #     The test_days_to_birthday function tests the days_to_birthday function in Record.py
    #         It does this by creating a mock date and then comparing it to the birthday of a record object.
    #         If they are equal, then the test passes.
    #     """
    #     current_date = datetime(2023, 1, 1)
        
    #     self.record_test.add_birthday('1-1-2000')
    #     self.assertEqual(self.record_test.days_to_birthday(current_date), 0)

    # def test_days_to_birthday_none(self) -> None:
    #     """
    #     The test_days_to_birthday_none function tests the days_to_birthday function in Record.py
    #         to see if it returns None when the current date is after the birthday of a record.
    #     """
    #     current_date = datetime(2023, 1, 1)
    #     self.assertEqual(self.record_test.days_to_birthday(current_date), None)

if __name__ == '__main__':
    unittest.main()
