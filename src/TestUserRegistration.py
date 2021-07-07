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
        """
        Description:
            this function validate mail
        """
        self.assertTrue(Validations.mailValidation("abc.xyz@bl.co.in"))
        

    def test_givenInvalidMail_shouldReturnFalse(self):
        """
        Description:
            this function validate invalid mail
        """
        self.assertFalse(Validations.mailValidation("abc.xyzbl.co.in"))
        self.assertFalse(Validations.mailValidation("abc.xyz@.co.in"))
        self.assertFalse(Validations.mailValidation("ab.cxyz@bl.co.in"))
        
    def test_givenValidPhoneNumber_shouldReturnTrue(self):
        """
        Description:
            this function validate mobile number
        """
        self.assertTrue(Validations.phoneValidation("91 2314569870"))
        

    def test_givenInvalidPhoneNumber_shouldReturnFalse(self):
        """
        Description:
            this function validate invalid mobile number
        """
        self.assertFalse(Validations.phoneValidation("9 1236547890"))
        self.assertFalse(Validations.phoneValidation("7896541230236"))
        self.assertFalse(Validations.phoneValidation("91 897456@231"))

    def test_givenValidPassword_shouldReturnTrue(self):
        """
        Description:
            this function validate password
        """
        self.assertTrue(Validations.passwordValidation("Swapnil@1"))
        

    def test_givenInvalidPassword_shouldReturnFalse(self):
        """
        Description:
            this function validate invalid mobile number
        """
        self.assertFalse(Validations.passwordValidation("Swapn@"))
        self.assertFalse(Validations.passwordValidation("@swapnil"))
        self.assertFalse(Validations.passwordValidation("abc"))


if __name__=="__main__":
    unittest.main()