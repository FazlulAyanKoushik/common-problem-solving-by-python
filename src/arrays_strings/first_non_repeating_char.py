def first_non_repeating_char(s: str):
    """
    Find the first non-repeating character in a string
    """
    for i in range(len(s)):
        # check if the character is not in the rest of the string,
        # and s[:i] uses slicing to get the characters before the current character
        if s[i] not in s[i + 1:] and s[i] not in s[:i]:
            return s[i]
    return None


# This is a more efficient solution
def first_non_repeating_char_(s: str):
    """
    Find the first non-repeating character in a string
    """
    # Create a dictionary to store the count of each character
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Loop through the string and return the first character with a count of 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None


if __name__ == '__main__':
    print(first_non_repeating_char('bnbgtogn'))
    print(first_non_repeating_char_('racecar'))
