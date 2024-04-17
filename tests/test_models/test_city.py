#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import os


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Testing state_id type."""
        new = self.value()
        expected_type = (
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
        self.assertEqual(type(new.state_id), expected_type)

    def test_name(self):
        """Testing name type."""
        new = self.value()
        expected_type = (
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
        self.assertEqual(type(new.name), expected_type)

    def test_relationship_places(self):
        """
        Test case to check if the 'places' attribute in the City model\
                is correctly defined as a relationship with the Place model.
        """
        new = self.value()
        self.assertTrue(hasattr(new, 'places'))
        self.assertIsInstance(new.places, relationship)
