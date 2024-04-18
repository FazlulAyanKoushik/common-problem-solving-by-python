def find_missing_number(arr):
    """
    Find the missing number in the array
    :param arr:
    :return:
    """
    # The length of the array is one more than the length of the original array
    n = len(arr) + 1

    # The sum of the first n natural numbers is n * (n + 1) / 2
    total = n * (n + 1) // 2

    return total - sum(arr)


if __name__ == '__main__':
    # Example usage:
    array = [1, 2, 4, 5]
    print(find_missing_number(array))
