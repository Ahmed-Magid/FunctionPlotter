from unittest import TestCase, main

from utils.Validator import Validator


class Test(TestCase):
    def setUp(self):
        self.validator = Validator()

    def testIsValidFunction1(self):
        function = 'x^2+x-9'
        result = self.validator.isValidFunction(function)
        self.assertTrue(result)

    def testIsValidFunction2(self):
        function = '3*x^2+5*x^'
        self.assertRaises(SyntaxError, lambda: self.validator.isValidFunction(function))

    def testIsValidFunction3(self):
        function = 'x^3+(1/(x^2))+3*(x+6)-9'
        result = self.validator.isValidFunction(function)
        self.assertTrue(result)

    def testIsValidFunction4(self):
        function = 'x^2+*3*x'
        self.assertRaises(SyntaxError, lambda: self.validator.isValidFunction(function))

    def testIsValidFunction5(self):
        function = 'Hello'
        self.assertRaises(SyntaxError, lambda: self.validator.isValidFunction(function))


if __name__ == '__main__':
    main()
