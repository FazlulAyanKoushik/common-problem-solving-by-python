def rotate_array(array):
    """
    Rotates the full array
    """
    # The length of the array
    n = len(array)

    # The rotated array
    rotated_array = []

    # Rotate the array
    for i in range(n-1, -1, -1):
        rotated_array.append(array[i])

    return rotated_array


if __name__ == '__main__':
    # Example usage:
    array = [1, 2, 4, 5]
    print(rotate_array(array))
