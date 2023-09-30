import unittest

## normal problem.
## To many problems.
## notation.
## Number only contain digits.
## Numbers cannot be more than four digits.
arranged_problems = ''
# print("-"*4)
top_row = '1112   3222'
bottom_row = '1 2'
dashes = "---- - "
dashes = dashes + "---- +"
solutions = f'1{" "*4}5'
arranged_problems = '\n'.join((top_row, bottom_row, dashes, solutions))

print(arranged_problems)