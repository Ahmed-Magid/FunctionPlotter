from numpy import arange

class FunctionManager:
    def prepareFunction(self, function: str) -> str:
        """
        Takes a function and prepares it to be evaluated by putting it in a mathematical form that can be evaluated in Python.
        :param function: The function to be prepared.
        :returns: The prepared function.
        """
        return function.replace(' ', '').replace('^', '**').replace('X', 'x')

    def substitute(self, function: str, value: str) -> str:
        """
        Substitutes the variable x from the function with an actual value to be evaluated.
        :param function: f(x) function.
        :param value: The value to substitute x with.
        :returns: The function after substitution.
        """

        return function.replace('x', value)

    def generateCoordinates(self, function: str, minValue: float, maxValue: float) -> tuple[list, list]:
        """
        Takes a function and returns a list of x values from min to max with the corresponding y values after substituting x with each value between min and max.
        :param function: The function to be evaluated from min to max.
        :param minValue: Minimum value for x.
        :param maxValue: Maximum value for x.
        :returns: A list of all x values with corresponding y values after substitution.
        """

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
