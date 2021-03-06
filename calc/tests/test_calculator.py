from calc.calculator import calculator as c
import unittest

#app.testing = True


# TODO: Extend these unit tests for the calculator module!


class TestAdd(unittest.TestCase):
    def test_add_integers_positive(self):
        result = c.sum(1, 2)
        self.assertEqual(result, 3)

    def test_add_integers_negative(self):
        result = c.sum(-1, -2)
        self.assertEqual(result, -3)

    def test_add_integers_pos_neg(self):
        result = c.sum(1, -2)
        self.assertEqual(result, -1)

    def test_add_integers_neg_pos(self):
        result = c.sum(-1, 2)
        self.assertEqual(result, 1)

    def test_divide_integers_positive(self):
        result = c.divide(6, 3)
        self.assertEqual(result, 2)

    def test_divide_integers_positive2(self):
        result = c.divide(7, 3)
        self.assertEqual(result, 2)

    def test_divide_integers_negative(self):
        result = c.divide(-6, -2)
        self.assertEqual(result, 3)

    def test_divide_integers_negative2(self):
        result = c.divide(-7, -2)
        self.assertEqual(result, 3)

    def test_divide_integers_pos_neg(self):
        result = c.divide(6, -2)
        self.assertEqual(result, -3)

    def test_divide_integers_pos_neg2(self):
        result = c.divide(9, -2)
        self.assertEqual(result, -4)

    def test_divide_integers_neg_pos(self):
        result = c.divide(-6, 2)
        self.assertEqual(result, -3)

    def test_divide_integers_neg_pos2(self):
        result = c.divide(-7, 2)
        self.assertEqual(result, -3)

    def test_divide_zero(self):
        result = c.divide(0, 2)
        self.assertEqual(result, 0)

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, c.divide, 6, 0)

    def test_multiply_integers_positive(self):
        result = c.multiply(6, 3)
        self.assertEqual(result, 18)

    def test_multiply_integers_positive2(self):
        result = c.multiply(7, 3)
        self.assertEqual(result, 21)

    def test_multiply_integers_negative(self):
        result = c.multiply(-6, -2)
        self.assertEqual(result, 12)

    def test_multiply_integers_negative2(self):
        result = c.multiply(-7, -2)
        self.assertEqual(result, 14)

    def test_multiply_integers_pos_neg(self):
        result = c.multiply(6, -2)
        self.assertEqual(result, -12)

    def test_multiply_integers_pos_neg2(self):
        result = c.multiply(9, -2)
        self.assertEqual(result, -18)

    def test_multiply_integers_neg_pos(self):
        result = c.multiply(-6, 2)
        self.assertEqual(result, -12)

    def test_multiply_integers_neg_pos2(self):
        result = c.multiply(-7, 2)
        self.assertEqual(result, -14)

    def test_multiply_zero(self):
        result = c.multiply(0, 2)
        self.assertEqual(result, 0)

    def test_multiply_zero2(self):
        result = c.multiply(3, 0)
        self.assertEqual(result, 0)

    def test_multiply_zero3(self):
        result = c.multiply(-3, 0)
        self.assertEqual(result, 0)

    def test_sub_integers_positive(self):
        result = c.subtract(1, 2)
        self.assertEqual(result, -1)

    def test_sub_integers_negative(self):
        result = c.subtract(-1, -2)
        self.assertEqual(result, 1)

    def test_sub_integers_pos_neg(self):
        result = c.subtract(1, -2)
        self.assertEqual(result, 3)

    def test_sub_integers_neg_pos1(self):
        result = c.subtract(-1, 2)
        self.assertEqual(result, -3)

    def test_sub_integers_neg_pos2(self):
        result = c.subtract(-1,0)
        self.assertEqual(result, -1)

    def test_sub_integers_neg_pos3(self):
        result = c.subtract(0,-5)
        self.assertEqual(result, 5)