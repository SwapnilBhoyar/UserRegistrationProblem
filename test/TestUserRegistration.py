"""
@Author: Swapnil Bhoyar
@Date: 2021-07-08 09:35:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-08-05 09:35:00
@Title : test for User registration program.
"""

import unittest
from  Validations import Validations
from TestInput import TestInput

class TestUserRegistration(unittest.TestCase):

    def test_givenValidName_shouldReturnTrue(self):
        """
        Description:
            this function validate name
        """
        self.assertTrue(Validations.firstNameValidation(TestInput.valiadName))

    def test_givenInalidName_shouldReturnFalse(self):
        """
        Description:
            this function validate inavalid name
        """
        self.assertFalse(Validations.nameValidation(TestInput.invaliadName))

    def test_givenValidLatName_shouldReturnTrue(self):
        """
        Description:
            this function validate last name
        """
        self.assertTrue(Validations.firstNameValidation(TestInput.valiadName))

    def test_givenInalidLastName_shouldReturnFalse(self):
        """
        Description: 
            this function validate invalid last name
        """
        self.assertFalse(Validations.lastNameValidation(TestInput.invaliadName))

    def test_givenValidMail_shouldReturnTrue(self):
        """
        Description:
            this function validate mail
        """
        self.assertTrue(Validations.validMailValidation(TestInput.valiadMail))
        

    def test_givenInvalidMail_shouldReturnFalse(self):
        """
        Description:
            this function validate invalid mail
        """
        self.assertFalse(Validations.mailValidation(TestInput.invaliadMail))
        
    def test_givenValidPhoneNumber_shouldReturnTrue(self):
        """
        Description:
            this function validate mobile number
        """
        self.assertTrue(Validations.validPhoneValidation(TestInput.valiadPhone))
        

    def test_givenInvalidPhoneNumber_shouldReturnFalse(self):
        """
        Description:
            this function validate invalid mobile number
        """
        self.assertFalse(Validations.phoneValidation(TestInput.invaliadPhone))

    def test_givenValidPassword_shouldReturnTrue(self):
        """
        Description:
            this function validate password
        """
        self.assertTrue(Validations.validPasswordValidation(TestInput.valiadPassword))
            
    def test_givenInvalidPassword_shouldReturnFalse(self):
        """
        Description:
            this function validate invalid mobile number
        """
        self.assertFalse(Validations.passwordValidation(TestInput.invaliadPassword))
    
    def test_givenValidMultipleMails_shouldReturnTrue(self):
        """
        Description:
            this function validate multiple mails
        """
        self.assertTrue(Validations.multipleMailValidation(TestInput.validMailIds))

    def test_givenInvalidMultipleMails_shouldReturnFalse(self):
        """
        Description:
            this function validate multiple invalid mails 
        """
        self.assertFalse(Validations.multipleMailValidation(TestInput.invalidMmailIds))

if __name__=="__main__":
    unittest.main()