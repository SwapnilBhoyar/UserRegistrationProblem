"""
@Author: Swapnil Bhoyar
@Date: 2021-07-05 18:42:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 18:42:00
@Title : validation for User registration program.
"""
import re
from Log import Log
from Patterns import Patterns
class Validations:

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
