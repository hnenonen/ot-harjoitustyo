import sympy as sp
import unittest
from services.math_service import Approximate


class TestMath(unittest.TestCase):
    def setUp(self):
        self.approx = Approximate()

    def test_define_works_correct_with_correct_input(self):
        self.assertEqual((self.approx.define("x**2")), sp.sympify("x**2"))

    def test_taylor_works_correct(self):
        self.assertEqual(
            (self.approx.taylor(sp.sympify("x**2"))), sp.sympify("2*x"))
