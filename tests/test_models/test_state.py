#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_cities_relationship(self):
        """
        Test case to check if the 'cities' relationship in the State model is
        correctly defined.
        """
        new_state = self.value()
        self.assertTrue(hasattr(new_state, 'cities'))
        self.assertEqual(type(new_state.cities), relationship)
