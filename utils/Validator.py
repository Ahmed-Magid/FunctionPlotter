from re import match


class Validator:
    def isValidFunction(self, function):
        if function == '':
            raise SyntaxError('Please fill the function field')
        regex = '(?:[0-9-+*/^()x])+'
        if not match(regex, function):
            raise SyntaxError('Invalid function.')
        testFunction = function.replace('x', '(1)').replace('^', '**')
        try:
            eval(testFunction)
        except Exception:
            raise SyntaxError('Invalid function')
        return True
