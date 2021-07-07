"""
@Author: Swapnil Bhoyar
@Date: 2021-07-05 18:42:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 18:42:00
@Title : test for User registration program.
"""

import unittest
from  Validations import Validations

class TestUserRegistration(unittest.TestCase):

    def test_givenValidName_shouldReturnTrue(self):
        self.assertTrue(Validations.nameValidation("Swapnil"))

    def test_givenValidName_shouldReturnFalse(self):
        self.assertFalse(Validations.nameValidation("swapnil"))
        self.assertFalse(Validations.nameValidation("swapnil123"))
        self.assertFalse(Validations.nameValidation("sw@pnil"))

    def test_givenValidLatName_shouldReturnTrue(self):
        self.assertTrue(Validations.lastNameValidation("Bhoyar"))

    def test_givenValidLastName_shouldReturnFalse(self):
        self.assertFalse(Validations.lastNameValidation("bhoyar"))
        self.assertFalse(Validations.lastNameValidation("bhoyar123"))
        self.assertFalse(Validations.lastNameValidation("bhoy@r"))



if __name__=="__main__":
    unittest.main()