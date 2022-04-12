from sympy import sympify, Symbol, factorial


class Approximate:

    def define(self, input_func):
        func = sympify(input_func)
        return func

    def taylor(self, func):
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
