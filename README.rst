Overview
========

Address Book as a prof of concept of OO design of a simple relationship between Groups and Persons stored in the same
AddressBook registry object

* AddressBook is a utility exposed as unified interface to deal with internal structure with simple API

* Basic entities used in the system is Person and Group. Group contains Persons.

* Person should know about Groups it belongs to. To simplify future extension of models and decouple
  class referencing, such reference is handled by the AddressBook utility. No circular referencing.

* As the main entity of the module is AddressBook, the design decision was made to made users aware of groups
  only in the scope of one AddressBook. To provide such information globally objects would have to be referenced
  to each other, which would complicate future extentions. The other possible way would be providing the global utility
  storing such references.

* Duck typing. There are no assumptions about Person and Group. There is no formal interface specified, but
  any class providing required methods may be used.

* Design-only questions: Find person by email address (can supply any substring, ie. "comp" should
  work assuming "alexander@company.com" is an email address in the address
  book) - discuss how you would implement this without coding the solution.

*  ANSWER: It was pretty easy to implement. Non-empty string is a substring to search for in email addresses.
   Email addresses are case-insensitive.


API
===

.. code-block:: python

   class Person:
       def __init__(self, first_name, last_name, street_addresses, email_addresses, phone_numbers)
 
   # Create the instance with provided parameters. All of them need to be non-empty.

.. code-block:: python

   class Group:
       def __init__(self, persons={})

   # Create a new group with optional set of Person instances


.. code-block:: python

   class AddressBook:
       def __init__(self, persons={}, groups={})

   # Create the instance of the address book. Initial set of Group and Person instances is optional

.. code-block:: python

   def add_person(self, person):

   # Add the instance of Person

.. code-block:: python

   def add_group(self,group):

   # Add the instance of Group

.. code-block:: python

   def get_person_groups(self, person):

   # Get all groups that provided person belongs to

.. code-block:: python

   def get_group_persons(self, group):

   # Get all persons that belong to specified group

.. code-block:: python

   def remove_person(self, person):

   # Remove the instance of Person

.. code-block:: python

   def remove_group(self, group):

   # Remove the instance of Group

.. code-block:: python

   def clean(self, group):

   # Clean users and groups

.. code-block:: python

   def get_persons_by_name(self, search_string='', first_name='', last_name='',
                           case_sensitive=False, equal=False):

   # Searching by provided strings.
   # 'search_string' is used instead of missing 'first_name' or 'last_name'.

.. code-block:: python

   def get_persons_by_email_address(self, email_address):

   # Searching by provided email address. Case insensite search for Person
   # objects with any email address including provided text.


Testing
=======

Unit tests provided. Module may be tested using the command

```python -m unittest discover```

