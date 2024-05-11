"""
Given a string s, find the length of the longest substring without repeating characters.
"""


"""leetcode solution"""


class Solution:
    def length_of_longest_substring(self, s: str):
        """
        Find the length of the longest substring without repeating characters
        """
        # Create a dictionary to store the index of each character
        subs_string_dict = {}
        subs_string = ""

        for i in range(len(s)):
            if s[i] not in subs_string:
                subs_string += s[i]
            else:
                subs_string_dict[subs_string] = len(subs_string)
                last_index_of_char = subs_string.rfind(s[i])
                subs_string = subs_string[last_index_of_char + 1:] + s[i]

        subs_string_dict[subs_string] = len(subs_string)

        # now return the maximum length of the substring and the substring itself
        max_length = max(subs_string_dict.values())
        return max_length


"""My Approach"""
# class Solution:
#     def length_of_longest_substring(self, s: str):
#         """
#         Find the length of the longest substring without repeating characters
#         """
#         # Create a dictionary to store the index of each character
#         subs_string_dict = {}
#         subs_string = ""
#
#         for i in range(len(s)):
#             if s[i] not in subs_string:
#                 subs_string += s[i]
#             else:
#                 subs_string_dict[subs_string] = len(subs_string)
#                 last_index_of_char = subs_string.rfind(s[i])
#                 subs_string = subs_string[last_index_of_char + 1:] + s[i]
#
#         subs_string_dict[subs_string] = len(subs_string)
#
#         # now return the maximum length of the substring and the substring itself
#         max_length = max(subs_string_dict.values())
#         max_substring = max(subs_string_dict, key=subs_string_dict.get)
#         return max_length, max_substring


if __name__ == '__main__':
    s = Solution()
    print(s.length_of_longest_substring('dvdf'))
    print(s.length_of_longest_substring('dbbacdf'))
    print(s.length_of_longest_substring('bbbbb'))
    print(s.length_of_longest_substring('pwwkew'))
    print(s.length_of_longest_substring(''))
    print(s.length_of_longest_substring(' '))
    print(s.length_of_longest_substring('au'))
    print(s.length_of_longest_substring('aab'))
    print(s.length_of_longest_substring('abba'))
