import unittest
# import pandas as pd
from arithmetic_arranger import arithmetic_arranger

## normal problem. (ok)
result = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
# result = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

## To many problems. (ok)
# result = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "123 + 49", "123 + 49"], True)

## notation. (ok)
# result = arithmetic_arranger(["32 / 698", "3801 - 2", "45 + 43", "123 + 49"], True)

## Number only contain digits. (ok)
# result = arithmetic_arranger(["ss + 698", "380 - 2", "45 + 43", "123 + 49"], True)

## Numbers cannot be more than four digits. (ok)
# result = arithmetic_arranger(["32 + 698", "553801 - 2", "45 + 43", "123 + 49"], True)
# result = arithmetic_arranger(["32 + 698", "2 - 553801", "45 + 43", "123 + 49"], True)

# print(result)

# print(len(result.split(" \n")))


class TestAritmaticFormatter(unittest.TestCase):
    def withResult(self):
        self.assertEqual(len(result.split(" \n")), 4)

    def noResult(self):
        self.assertEqual(len(result.split(" \n")), 3)

    def manyProblem(self):
        with self.assertRaisesRegex(TypeError, "Too many problems."):
            arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "123 + 49", "123 + 49"], True)

    def notation(self):
        with self.assertRaisesRegex(TypeError, "Operator must be '+' or '-'."):
            arithmetic_arranger(["32 / 698", "3801 - 2", "45 + 43", "123 + 49"], True)

    def onlyContainDigit(self):
        with self.assertRaisesRegex(ValueError, "Numbers must only contain digits."):
            arithmetic_arranger(["ss + 698", "380 - 2", "45 + 43", "123 + 49"], True)

    def moreThanFourDigit(self):
        with self.assertRaisesRegex(TypeError, "Numbers cannot be more than four digits."):
            arithmetic_arranger(["32 + 698", "553801 - 2", "45 + 43", "123 + 49"], True)


# unittest.main()