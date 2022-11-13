import unittest

from phonebook import phonebook

class PhoneBookTest(unittest.Testcase):

    def test_lookup_by_name(self):
        phonebook = PhoneBook()
        phonebook.add("Sofia", "0700433078")
        number = phonebook.lookup("Sofia")
        self.assertEqual("070033078", number)
        