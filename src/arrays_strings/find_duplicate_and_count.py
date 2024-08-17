"""
Problem: Find duplicate and count
Given an array of integers, find the number of duplicate elements in the array.

Example:
    array = [1, 2, 3, 4, 2, 3, 1, 2, 3, 4, 2, 3]
    Frequency of each number:
        1: 2
        2: 4
        3: 4
        4: 2
"""

from typing import List


class Solution:
    def findDuplicateAndCount(self, nums: List[int]) -> dict:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        #return those numbers that have a frequency greater than 1
        return {num: count for num, count in freq.items() if count > 1}


if __name__ == '__main__':
    # Example usage:
    array = [1, 2, 3, 4, 2, 3, 1, 2, 3, 2, 3]
    solution = Solution()
    print(solution.findDuplicateAndCount(array))
