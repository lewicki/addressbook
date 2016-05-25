# -*- coding: utf-8 -*-


class Person(object):
    """
    Base class to implement required interface
    :first_name: string
    :last_name: string
    :street_addresses: list
    :email_addresses: list
    :phone_numbers: list
    """
    def __init__(self, first_name, last_name, street_addresses, email_addresses, phone_numbers):
        # checking if all obligatory parameters are provided
        if not all([first_name, last_name, street_addresses, email_addresses, phone_numbers]):
            raise AttributeError('Not all parameters provided')
        self.first_name = first_name
        self.last_name = last_name
        self.street_addresses = street_addresses[:]
        self.email_addresses = email_addresses[:]
        self.phone_numbers = phone_numbers[:]

    def add_to_group(self, group):
        self.groups.add(group)

    def remove_from_group(self, group):
        self.groups.discard(group)

    @staticmethod
    def check_match(field_value, value, case_sensitive=False, equal=False):
        """
        Generic method to compare stings
        """
        if case_sensitive:
            if equal:
                return value == field_value
            else:
                return value in field_value
        else:
            if equal:
                return value.lower() == field_value.lower()
            else:
                return value.lower() in field_value.lower()

    def get_by_name(self, search_string='', first_name='', last_name='', case_sensitive=False, equal=False):
        """
        Searching by provided strings.
        'search_string' is used instead of missing 'first_name' or 'last_name'.
        :param search_string:
        :param first_name:
        :param last_name:
        :param case_sensitive:
        :param equal:
        :return: True if matching
        """
        first_name = first_name or search_string
        last_name = last_name or search_string
        first_name_check = self.check_match(self.first_name, first_name, case_sensitive) if first_name else False
        last_name_check = self.check_match(self.last_name, last_name, case_sensitive) if last_name else False
        return first_name_check or last_name_check

    def get_by_email_address(self, email_address):
        """
        Searching by provided email address. Case insensite search for Person
        objects with any email address including provided text.
        :param email_address:
        :return: True if matching
        """
        if not email_address:
            return False
        filtered = [adr_to_check for adr_to_check in self.email_addresses
                    if adr_to_check and self.check_match(adr_to_check, email_address)]
        return True if filtered else False
