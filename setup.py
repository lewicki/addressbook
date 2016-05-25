from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='addressbook',
      version=version,
      description="Test implementaion of searchable addressbook",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Pawel Lewicki',
      author_email='pawel.lewicki@gmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
