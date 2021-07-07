import unittest
from  Validations import Validations

class TestUserRegistration(unittest.TestCase):

    def test_givenValidName_shouldReturnTrue(self):
        self.assertTrue(Validations.nameValidation("Swapnil"))

    def test_givenValidName_shouldReturnFalse(self):
        self.assertFalse(Validations.nameValidation("swapnil"))
        self.assertFalse(Validations.nameValidation("swapnil123"))
        self.assertFalse(Validations.nameValidation("sw@pnil"))


if __name__=="__main__":
    unittest.main()