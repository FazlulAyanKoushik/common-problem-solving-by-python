"""
Sort a list without using the sort function
"""

my_list = [5, 4, -4, -3, -5, 3, 2, 1, 1, 2]


def sort_list(lst):
    """
    Sort a list without using the sort function
    """
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] >= lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    return lst


print(sort_list(my_list))
