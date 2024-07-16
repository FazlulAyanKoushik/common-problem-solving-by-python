"""2404. Most Frequent Even Number

    Given an array of integers, find the most frequent even number in the array. If there are multiple numbers that
    appear the same number of times, return the smallest one. If there are no even numbers in the array, return -1.

    Example 1:
        Input: [1, 2, 2, 3, 3, 3]
        Output: 2

    Example 2:
        Input: [1, 1, 1, 3, 3, 3]
        Output: -1

    Example 3:
        Input: [1, 2, 2, 3, 3, 3, 4, 4, 4]
        Output: 2


    Constraints:
        1 <= nums.length <= 2000
        0 <+ nums[i] <= 10^5 that is, 0 <= nums[i] <= 100000
"""

from typing import List

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            if num % 2 == 0:
                counts[num] = counts.get(num, 0) + 1

        if not counts:
            return -1

        highest_freq = 0
        smallest_num = 0
        for num, freq in counts.items():
            if freq > highest_freq:
                highest_freq = freq
                smallest_num = num
            elif freq == highest_freq and num < smallest_num:
                smallest_num = num
        return smallest_num


if __name__ == '__main__':
    # Example usage:
    array = [1, 2, 2, 3, 3, 3]
    solution = Solution()
    print(solution.mostFrequentEven(array))
    array = [1, 1, 1, 3, 3, 3]
    print(solution.mostFrequentEven(array))
    array = [1, 2, 2, 3, 3, 3, 4, 4, 4]
    print(solution.mostFrequentEven(array))
    array = [1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4]
    print(solution.mostFrequentEven(array))
    array = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    print(solution.mostFrequentEven(array))