def check_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome
    """
    # return s == s[::-1]
    copied = s
    for i in range(len(s) // 2):  # // is floor division, ex: 5 // 2 = 2
        if s[i] == copied[-i - 1]:  # check if the first and last characters are the same and so on
            return True
        else:
            return False


if __name__ == '__main__':
    print(check_palindrome('racecar'))
