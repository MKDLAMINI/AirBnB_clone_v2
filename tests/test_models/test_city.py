#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_relationship_places(self):
        """
        Test case to check if the 'places' attribute in the City model\
                is correctly defined as a relationship with the Place model.
        """
        new = self.value()
        self.assertTrue(hasattr(new, 'places'))
        self.assertIsInstance(new.places, relationship)
