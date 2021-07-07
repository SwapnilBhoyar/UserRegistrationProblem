"""
@Author: Swapnil Bhoyar
@Date: 2021-07-05 18:42:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 18:42:00
@Title : pattern for validation.
"""
class Patterns:
    NAME_PATTERN = r"^[A-Z]{1}[a-zA-Z]{2,}$"
    MAIL_PATTERN = "^[a-zA-Z0-9]{3,}([\\.\\+\\-]?[a-zA-Z0-9]{3,})?[@][A-Za-z0-9]{1,}[.][A-Za-z]{2,4}[,]?([.][A-Za-z]{2,4}[.]?)?$"