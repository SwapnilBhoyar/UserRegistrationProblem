"""
@Author: Swapnil Bhoyar
@Date: 2021-07-08 09:35:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-08 09:35:00
@Title : validation for User registration program.
"""
import re
from Log import Log
from Patterns import Patterns
class Validations:

    validMailIds = ["abc@yahoo.com", "abc-100@yahoo.com",
                      "abc.100@yahoo.com", "abc111@abc.com", "abc-100@abc.net", "abc.100@abc.com.au", "abc@1.com",
                      "abc@gmail.com.com", "abc+100@gmail.com"]

    invalidMmailIds = ["abc@.com.my", "abc123@gmail.a", "abc123@.com",
                        "abc123@.com.com", ".abc@abc.com", "abc()*@gmail.com", "abc..2002@gmail.com", "abc.@gmail.com",
                        "abc@abc@gmail.com", "abc@gmail.com.1a", "abc@gmail.com.aa.au"]

    def nameValidation(name):
        """
        Description:
            this function validate name
        """
        try:
            return (re.match(re.compile(Patterns.NAME_PATTERN), name))
        except Exception as e:
            Log.logger.error(e)

    def lastNameValidation(name):
        """
        Description:
            this function validate name
        """
        try:
            return (re.match(re.compile(Patterns.NAME_PATTERN), name))
        except Exception as e:
            Log.logger.error(e)

    def mailValidation(mail):
        """
        Description:
            this function validate mail
        """
        try:
            return (re.match(re.compile(Patterns.MAIL_PATTERN), mail))
        except Exception as e:
            Log.logger.error(e)

    def phoneValidation(phone):
        """
        Description:
            this function validate mobile number
        """
        try:
            return (re.match(re.compile(Patterns.PHONE_PATTERN), phone))
        except Exception as e:
            Log.logger.error(e)

    def passwordValidation(password):
        """
        Description:
            this function validate passwords
        """
        try:
            return (re.match(re.compile(Patterns.PASSWORD), password))
        except Exception as e:
            Log.logger.error(e)

    def multipleMailValidation(validMailIds):
        """
        Description:
            this function validate multiple mails
        """
        try:
            for mail in validMailIds:
                return (re.match(re.compile(Patterns.MAIL_PATTERN), mail))
        except Exception as e:
            Log.logger.error(e)
