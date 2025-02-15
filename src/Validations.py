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

    def firstNameValidation(name):
        """
        Description:
            this function validate name
        """
        try:
            return re.match(re.compile(Patterns.NAME_PATTERN), name)
        except Exception as e:
            Log.logger.error(e)

    def nameValidation(name):
        """
        Description:
            this function validate name
        """
        try:
            for firstName in name:
                return re.match(re.compile(Patterns.NAME_PATTERN), firstName)
        except Exception as e:
            Log.logger.error(e)

    def lastNameValidation(name):
        """
        Description:
            this function validate name
        """
        try:
            for lastName in name:
                return (re.match(re.compile(Patterns.NAME_PATTERN), lastName))
        except Exception as e:
            Log.logger.error(e)

    def validMailValidation(mail):
        """
        Description:
            this function validate mail
        """
        try:
            return (re.match(re.compile(Patterns.MAIL_PATTERN), mail))
        except Exception as e:
            Log.logger.error(e)

    def mailValidation(mails):
        """
        Description:
            this function validate mail
        """
        try:
            for mail in mails:
                return (re.match(re.compile(Patterns.MAIL_PATTERN), mail))
        except Exception as e:
            Log.logger.error(e)

    def validPhoneValidation(phone):
        """
        Description:
            this function validate mobile number
        """
        try:
            return (re.match(re.compile(Patterns.PHONE_PATTERN), phone))
        except Exception as e:
            Log.logger.error(e)

    def phoneValidation(phones):
        """
        Description:
            this function validate mobile number
        """
        try:
            for phone in phones:
                    return (re.match(re.compile(Patterns.PHONE_PATTERN), phone))
        except Exception as e:
            Log.logger.error(e)

    def validPasswordValidation(password):
        """
        Description:
            this function validate passwords
        """
        try:
            return re.match(re.compile(Patterns.PASSWORD), password)
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
