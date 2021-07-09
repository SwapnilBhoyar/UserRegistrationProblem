"""
@Author: Swapnil Bhoyar
@Date: 2021-07-08 09:35:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-08-09 08:24:00
@Title : test for User registration program.
"""

import pytest
from Validations import Validations
from TestInput import TestInput

class TestUserRegistrationPytest:

    def test_givenValidFirstName_shouldReturnTrue(self):
        """
        Description:
            this function validate name
        """
        assert Validations.firstNameValidation(TestInput.valiadName)

    def test_givenInvalidName_shouldReturnFalse(self):
        """
        Description:
            this function validate inavalid name
        """
        assert not Validations.nameValidation(TestInput.invaliadName)

    def test_givenValidLatName_shouldReturnTrue(self):
        """
        Description:
            this function validate last name
        """
        assert Validations.firstNameValidation(TestInput.valiadName)

    def test_givenInalidLastName_shouldReturnFalse(self):
        """
        Description: 
            this function validate invalid last name
        """
        assert not Validations.lastNameValidation(TestInput.invaliadName)

    def test_givenValidMail_shouldReturnTrue(self):
        """
        Description:
            this function validate mail
        """
        assert Validations.validMailValidation(TestInput.valiadMail)
        

    def test_givenInvalidMail_shouldReturnFalse(self):
        """
        Description:
            this function validate invalid mail
        """
        assert not Validations.mailValidation(TestInput.invaliadMail)
        
    def test_givenValidPhoneNumber_shouldReturnTrue(self):
        """
        Description:
            this function validate mobile number
        """
        assert Validations.validPhoneValidation(TestInput.valiadPhone)
        
    def test_givenValidPassword_shouldReturnTrue(self):
        """
        Description:
            this function validate password
        """
        assert Validations.validPasswordValidation(TestInput.valiadPassword)

    def test_givenInvalidPhoneNumber_shouldReturnFalse(self):
        """
        Description:
            this function validate invalid mobile number
        """
        assert not Validations.phoneValidation(TestInput.invaliadPhone)
        
    def test_givenValidPassword_shouldReturnTrue(self):
        """
        Description:
            this function validate password
        """
        assert Validations.validPasswordValidation(TestInput.valiadPassword)
        
    
    def test_givenValidMultipleMails_shouldReturnTrue(self):
        """
        Description:
            this function validate multiple mails
        """
        assert Validations.multipleMailValidation(TestInput.validMailIds)

    def test_givenInvalidMultipleMails_shouldReturnFalse(self):
        """
        Description:
            this function validate multiple invalid mails 
        """
        assert not Validations.multipleMailValidation(TestInput.invalidMmailIds)