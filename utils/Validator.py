from re import match
from mathematics.FunctionManager import FunctionManager


class Validator:
    def __init__(self):
        self.functionManager = FunctionManager()

    def isValidFunction(self, function: str) -> bool:
        """
        Determines whether the given function is in a correct mathematical function form.
        :param function: The function to be tested.
        :raises SyntaxError: If the given function is not in a correct mathematical form.
        :returns: True if the function is in a correct mathematical form.
        """

        if function == '':
            raise SyntaxError('Please fill the function field')
        regex = '(?:[0-9-+*/^()xX])+'
        if not match(regex, function):
            raise SyntaxError('Invalid function.')
        testFunction = self.functionManager.prepareFunction(function)
        testFunction = self.functionManager.substitute(testFunction, '(1)')
        try:
            eval(testFunction)
        except Exception:
            raise SyntaxError('Invalid function')
        return True
