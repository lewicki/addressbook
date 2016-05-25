# -*- coding: utf-8 -*-


class Group(object):
    """
    Representation of group of Person instances
    """

    def __init__(self, persons=None):
        persons = persons if persons else {}
        self.persons = set(persons)

    def get_persons(self):
        return self.persons

    def add_person(self, person):
        return self.persons.add(person)

    def remove_person(self, person):
        return self.persons.discard(person)

    def has_person(self, persons):
        return persons in self.persons
