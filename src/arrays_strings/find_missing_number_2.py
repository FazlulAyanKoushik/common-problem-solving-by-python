"""
268. Missing Number
    Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is
    missing from the array.

    Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

    Example 1:
    Input: nums = [3,0,1]
    Output: 2

    Example 2:
    Input: nums = [0,1]
    Output:
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        sum_new_nums = n * (n - 1) // 2
        sum_nums = sum(nums)
        return sum_new_nums - sum_nums


if __name__ == '__main__':
    # Example usage:
    array = [0, 1, 2, 3, 5]
    solution = Solution()
    print(solution.missingNumber(array))
