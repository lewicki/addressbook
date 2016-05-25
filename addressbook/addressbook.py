# -*- coding: utf-8 -*-
# Python 3.5 compatibility
try:
    from functools import reduce
except:
    pass


class AddressBook(object):
    """
    Collection of people and groups
    """
    persons = []
    groups = []

    def __init__(self, persons={}, groups={}):
        """

        :param persons: iterable (list/set) of Person objects
        :param groups:iterable (list/set) of Group objects

        """
        self.persons = set(persons)
        self.groups = set(groups)

    def add_person(self, person):
        """
        :param person: Person object
        :return
        """
        self.persons.add(person)

    def add_group(self, group):
        """
        :param group: Group object
        :return
        """
        self.groups.add(group)

    def get_person_groups(self, person):
        """
        Get all groups that provided person belongs to
        :param person: Person object
        :return: set of Group objects
        """
        return {group for group in self.groups if group.has_person(person)}

    def get_group_persons(self, group):
        """
        Get all persons that belong to specified group
        :param group: Group object
        :return: set of Person objects
        """
        if group not in self.groups:
            raise AttributeError('Group {0} not in address book groups'.format(group))
        return group.get_persons()

    def remove_group(self, group):
        """
        :param group: Group object
        :return
        """
        self.groups.discard(group)

    def remove_person(self, person):
        """
        :param person: Person object
        :return
        """
        self.persons.discard(person)

    def clean(self):
        """
        Clean users and groups
        :return
        """
        self.persons = set([])
        self.groups = set([])

    def get_persons_by_name(self, search_string='', first_name='', last_name='', case_sensitive=False, equal=False):
        """
        Searching by provided strings.
        'search_string' is used instead of missing 'first_name' or 'last_name'.
        :param search_string:
        :param first_name:
        :param last_name:
        :param case_sensitive:
        :param equal:
        :return: set of matching Person objects
        """
        group_persons = [group.get_persons() for group in self.groups]
        persons = reduce(set.union, group_persons + [self.persons])
        filtered = {person for person in persons if person.get_by_name(search_string=search_string,
                                                                       first_name=first_name,
                                                                       last_name=last_name,
                                                                       case_sensitive=case_sensitive, equal=equal)}
        return filtered

    def get_persons_by_email_address(self, email_address):
        """
        Searching by provided email address. Case insensite search for Person
        objects with any email address including provided text.
        :param email_address:
        :return: set of matching Person objects
        """
        group_persons = [group.get_persons() for group in self.groups]
        persons = reduce(set.union, group_persons + [self.persons])
        filtered = {person for person in persons if person.get_by_email_address(email_address)}
        return filtered
