# Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary.
# o Sample data: {'1': ['a','b'], '2': ['c','d']}
# o Expected Output:
# o ac ad bc bd

from itertools import product

data={'1':['a','b'],'2':['c','d']}

values=list(data.values())
combinations=list(product(*values))

result=[''.join(combination) for combination in combinations]

print(' '.join(result))


