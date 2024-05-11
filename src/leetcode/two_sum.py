"""
Given an unsorted list of numbers and a target sum 'n',
write a function to determine whether there are two numbers in the list whose sum equals 'n'.
If such a pair exists, return True; otherwise, return False.
"""

numbers = [2, 4, 6, 7, 10]

n = 11


def sum_equal_of_n(numbers, n):
    """
    Check if there are two numbers in the list whose sum equals 'n'
    """
    for i in numbers:
        sub = n - i
        if sub in numbers:
            print(f'{i} + {sub} = {n}')
            return True
    return False


print(sum_equal_of_n(numbers, n))
