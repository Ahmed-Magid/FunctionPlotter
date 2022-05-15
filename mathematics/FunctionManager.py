from numpy import arange

class FunctionManager:
    def prepareFunction(self, function):
        function = function.replace(' ', '').replace('^', '**').replace('X', 'x')
        return function

    def substitute(self, function, value):
        return function.replace('x', value)

    def generateCoordinates(self, function, minValue, maxValue):
        xCoordinates = []
        yCoordinates = []
        for i in arange(minValue, maxValue + 1):
            actualFunction = self.substitute(function, '(' + str(i) + ')')
            try:
                yCoordinates.append(eval(actualFunction))
                xCoordinates.append(i)
            except ZeroDivisionError:
                pass
        return xCoordinates, yCoordinates
