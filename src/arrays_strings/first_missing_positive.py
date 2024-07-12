"""41. First Missing Positive
    Given an unsorted integer array nums, find the smallest missing positive integer.

    You must implement an algorithm that runs in O(n) time and uses constant extra space.

    Example 1:
    Input: nums = [1,2,0]
    Output: 3

    Example 2:
    Input: nums = [3,4,-1,1]
    Output: 2

    Example 3:
    Input: nums = [7,8,9,11,12]
    Output: 1

    Constraints:
    0 <= nums.length <= 300
    -231 <= nums[i] <= 231 - 1
"""
from typing import List
import unittest


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        count = 1
        nums = sorted(nums)
        for num in nums:
            if num < count:
                continue
            if num == count:
                count += 1
            else:
                return count
        return count


if __name__ == '__main__':
    array = [1, 2, 0]
    solution = Solution()
    print(solution.firstMissingPositive(array))
