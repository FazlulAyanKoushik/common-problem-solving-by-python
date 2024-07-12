"""
Find the missing number in the array [1, 2, 3, ..., n] where n is the length of the array

Example:
    array = [1, 2, 4, 5]
    find_missing_number(array) => 3
"""
def find_missing_number(arr):
    """
    Find the missing number in the array [1, 2, 3, ..., n] where n is the length of the array
    :param arr:
    :return:
    """
    # The length of the array is one more than the length of the original array
    n = len(arr) + 1
    print("n: ", n)

    # The sum of the first n natural numbers is n * (n + 1) / 2
    total = n * (n + 1) // 2
    print("Total: ", total)

    return total - sum(arr)


if __name__ == '__main__':
    # Example usage:
    array = [1, 2, 4, 5]
    # array = [0, 1, 2, 3, 5]
    print(find_missing_number(array))

