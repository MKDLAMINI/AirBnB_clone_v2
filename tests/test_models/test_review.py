#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)

    def test_text_length(self):
        """
        Test case to check if the 'text' attribute in the Review model\
                enforces the maximum length constraint.
        """
        new = self.value()
        max_length = 1024
        long_text = "a" * (max_length + 1)
        new.text = long_text
        self.assertRaises(ValueError, setattr, new, 'text', long_text)
