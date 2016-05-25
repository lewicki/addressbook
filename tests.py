import unittest
from addressbook.person import Person
from addressbook.group import Group
from addressbook.addressbook import AddressBook


class PersonTest(unittest.TestCase):
    def test_add_person(self):
        self.assertRaises(AttributeError, Person, 'First name', '', ['street'], ['expresident@archive.org'], ['112'])


class AddressBookTest(unittest.TestCase):

    def setUp(self):
        self.p1 = Person('Joe', 'Doe', ['street1'], ['joe@doe.com'], ['12345'])
        self.p2 = Person('Bill', 'Murray', ['street2'], ['bill@Murray.com'], ['1234567'])
        self.p3 = Person('Douglas', 'Adams', ['street3'], ['Douglas@Adams.com'], ['123456789'])
        self.g1 = Group([self.p2, self.p3])
        self.address_book = AddressBook(persons=[self.p1, self.p2], groups=[self.g1])

    def test_add_person(self):
        p = Person('Abraham', 'Lincoln', ['Lincoln Street 123'], ['expresident@archive.org'], ['112'])
        self.assertEqual(len(self.address_book.persons), 2)
        self.address_book.add_person(p)
        self.assertEqual(len(self.address_book.persons), 3)

    def test_add_group(self):
        p = Person('Abraham', 'Lincoln', ['Lincoln Street 123'], ['expresident@archive.org'], ['112'])
        g = Group([p])
        self.assertEqual(len(self.address_book.groups), 1)
        self.address_book.add_group(g)
        self.assertEqual(len(self.address_book.groups), 2)

    def test_get_person_groups(self):
        p = Person('Abraham', 'Lincoln', ['Lincoln Street 123'], ['expresident@archive.org'], ['112'])
        groups = self.address_book.groups
        self.assertEqual(len(self.address_book.get_person_groups(p)), 0)
        for group in groups:
            group.add_person(p)
        self.assertEqual(len(self.address_book.get_person_groups(p)), len(groups))

    def test_get_group_persons(self):
        self.assertEqual({self.p2, self.p3}, self.address_book.get_group_persons(self.g1))

    def test_get_persons_by_search_string_case_sensitive(self):
        self.assertEqual({self.p2}, self.address_book.get_persons_by_name('Murray', case_sensitive=True))
        self.assertEqual(set([]), self.address_book.get_persons_by_name('murray', case_sensitive=True))

    def test_get_persons_by_search_string_case_insensitive(self):
        self.assertEqual({self.p2}, self.address_book.get_persons_by_name('Murray'))
        self.assertEqual({self.p2}, self.address_book.get_persons_by_name('murray'))

    def test_get_persons_by_first_name(self):
        self.assertEqual({self.p2}, self.address_book.get_persons_by_name(first_name='Bill'))
        self.assertEqual(set([]), self.address_book.get_persons_by_name(first_name='Murray'))

    def test_get_persons_by_last_name(self):
        self.assertEqual(set([]), self.address_book.get_persons_by_name(last_name='Bill'))
        self.assertEqual({self.p2}, self.address_book.get_persons_by_name(last_name='Murray'))

    def test_get_persons_by_email_address(self):
        self.assertEqual({self.p1}, self.address_book.get_persons_by_email_address('Joe@Doe.com'))
        self.assertEqual({self.p1}, self.address_book.get_persons_by_email_address('joe@doe.com'))
        self.assertEqual({self.p1}, self.address_book.get_persons_by_email_address('Doe'))

    def test_remove_person(self):
        p = Person('Abraham', 'Lincoln', ['Lincoln Street 123'], ['expresident@archive.org'], ['112'])
        no_persons = len(self.address_book.persons)
        self.assertEqual(len(self.address_book.persons), no_persons)
        self.address_book.add_person(p)
        self.assertEqual(len(self.address_book.persons), no_persons+1)
        self.address_book.remove_person(p)
        self.assertEqual(len(self.address_book.persons), no_persons)

    def test_remove_group(self):
        g = Group()
        no_groups = len(self.address_book.groups)
        self.assertEqual(len(self.address_book.groups), no_groups)
        self.address_book.add_group(g)
        self.assertEqual(len(self.address_book.groups), no_groups + 1)
        self.address_book.remove_group(g)
        self.assertEqual(len(self.address_book.groups), no_groups)

    def test_clean(self):
        p = Person('Abraham', 'Lincoln', ['Lincoln Street 123'], ['expresident@archive.org'], ['112'])
        self.address_book.add_person(p)
        g = Group()
        self.address_book.add_group(g)
        no_groups = len(self.address_book.groups)
        no_persons = len(self.address_book.persons)
        self.assertEqual(len(self.address_book.groups), no_groups)
        self.assertEqual(len(self.address_book.persons), no_persons)
        self.address_book.clean()
        self.assertEqual(len(self.address_book.groups), 0)
        self.assertEqual(len(self.address_book.persons), 0)
