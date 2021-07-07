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
        """
        Description:
            this function validate name
        """
        self.assertTrue(Validations.nameValidation("Swapnil"))

    def test_givenInalidName_shouldReturnFalse(self):
        """
        Description:
            this function validate inavalid name
        """
        self.assertFalse(Validations.nameValidation("swapnil"))
        self.assertFalse(Validations.nameValidation("swapnil123"))
        self.assertFalse(Validations.nameValidation("sw@pnil"))

    def test_givenValidLatName_shouldReturnTrue(self):
        """
        Description:
            this function validate last name
        """
        self.assertTrue(Validations.lastNameValidation("Bhoyar"))

    def test_givenInalidLastName_shouldReturnFalse(self):
        """
        Description: 
            this function validate invalid last name
        """
        self.assertFalse(Validations.lastNameValidation("bhoyar"))
        self.assertFalse(Validations.lastNameValidation("bhoyar123"))
        self.assertFalse(Validations.lastNameValidation("bhoy@r"))

    def test_givenValidMail_shouldReturnTrue(self):
        self.assertTrue(Validations.mailValidation("abc.xyz@bl.co.in"))
        """
        Description:
            this function validate mail
        """

    def test_givenInvalidLastName_shouldReturnFalse(self):
        """
        Description:
            this function validate invalid mail
        """
        self.assertFalse(Validations.mailValidation("abc.xyzbl.co.in"))
        self.assertFalse(Validations.mailValidation("abc.xyz@.co.in"))
        self.assertFalse(Validations.mailValidation("ab.cxyz@bl.co.in"))

if __name__=="__main__":
    unittest.main()