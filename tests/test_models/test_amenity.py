#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ Test class for the Amenity model. """

    def __init__(self, *args, **kwargs):
        """ Initialize the test class. """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ Test case to check initialization of 'name' attribute.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_name_attribute(self):
        """
        Test case to check initialization of the 'name' attribute.

        Creates a new instance of the Amenity class and asserts that
        the 'name' attribute is an empty string.
        """
        new = self.value()
        self.assertEqual(new.name, "")

    def test_name_attribute_set(self):
        """
        Test case to check if the 'name' attribute is set correctly.

        Creates a new instance of the Amenity class and sets the 'name'
        attribute to a specific value. Asserts that the value of 'name'
        is correctly set.
        """
        new = self.value(name="Swimming Pool")
        self.assertEqual(new.name, "Swimming Pool")
