#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)

    def test_places_relationship(self):
        """
        Test case to check if the 'places' relationship in the User model is
        correctly defined.
        """
        new_user = self.value()
        self.assertTrue(hasattr(new_user, 'places'))
        self.assertEqual(type(new_user.places), relationship)

    def test_reviews_relationship(self):
        """
        Test case to check if the 'reviews' relationship in the User model is
        correctly defined.
        """
        new_user = self.value()
        self.assertTrue(hasattr(new_user, 'reviews'))
        self.assertEqual(type(new_user.reviews), relationship)
