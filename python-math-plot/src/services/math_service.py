from sympy import *
import matplotlib.pyplot as plt

class Approximate:

    def define(self, s):
        #s = input("enter a formula: ")
        #s =  "cos(x)"
        # "(x-1)**6"
        # enter a formula: sin(x) + x**3
        #'sin(x) + x**3'
        y = sympify(s)
        #x = Symbol('x')
        #self.taylor(y, x)            #calculate taylor polynomial
        #print(y)
        return y

    def taylor(self, y):
        x = Symbol('x')
        func = y
        list = []
        list.append(y)
        exprs = []

        n = 6
        i = 0
        while i < n:
            y = y.diff(x)
            a = y.subs(x, 0)
            exprs.append(a)
            list.append(y)
            i += 1
        f = str(func.subs(x, 0))
        constants = []
        for j in range(1, n):
            con = exprs[j] / factorial(j)
            if con > 0:
                constants.append(con)
                f += "+"
                f += "("+str(con)+"*x**"+str(j)+")"
        t = sympify(f)
        #self.plotting(func, t)           #calculate taylor polynomial and function
        #print(t)
        return t

    
