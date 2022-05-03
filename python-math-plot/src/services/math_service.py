from sympy import sympify, Symbol, factorial

class Approximate:

    """Class, that takes user input function and appromixates a Taylor polynom based on it.
    """
    
    def define(self, input_func):

        """Prepares user input string into a function for sympify to use
        Args: 
            input_func: function to be approximated from user as a String
        Returns:
            func: function to be approximated as a Sympify function
        """

        func = sympify(input_func)
        return func

    def taylor(self, func):

        """Takes a function and creates a taylor polynom of 5th degree 
            by calculating the fifth derivative of the function.
        Args:
            func: Sympified function from user
        Returns:
            taylor_approx: Sympified taylor polynom created by the method
        """

        respect_to_x = Symbol('x')
        list = []
        list.append(func)
        expressions = []
        degree_accuracy = 6
        counter = 0

        while counter < degree_accuracy:
            func = func.diff(respect_to_x)
            const_0 = func.subs(respect_to_x, 0)
            expressions.append(const_0)
            list.append(func)
            counter += 1
        taylor_f = str(func.subs(respect_to_x, 0))
        constants = []

        for j in range(1, degree_accuracy):
            con = expressions[j] / factorial(j)
            if con > 0:
                constants.append(con)
                taylor_f += "+"
                taylor_f += "("+str(con)+"*x**"+str(j)+")"
        taylor_approx = sympify(taylor_f)
        
        return taylor_approx
