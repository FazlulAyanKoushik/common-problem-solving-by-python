"""
Given an unsorted list of numbers and a target sum 'n',
write a function to determine whether there are two numbers in the list whose sum equals 'n'.
If such a pair exists, return True; otherwise, return False.
"""

from typing import List


unsorted_list = [10, 15, 3, 7, 4]
sorted_list = sorted(unsorted_list)

_sum = 11


def sum_equal_of_n(numbers: List[int], _sum: int) -> bool:
    """
    Check if there are two numbers in the list whose sum equals 'n'
    """
    for i in numbers:
        sub = _sum - i
        if sub in numbers:
            print(f'{i} + {sub} = {_sum}')
            return True
    return False


print(sum_equal_of_n(sorted_list, _sum))
