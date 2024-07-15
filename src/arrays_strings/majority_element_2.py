"""229. Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Follow-up: Could you solve the problem in linear time and in O(1) space?

Example 1:
    Input: nums = [3,2,3]
    Output: [3]

Example 2:
    Input: nums = [1]
    Output: [1]

Example 3:
    Input: nums = [1,2]
    Output: [1,2]
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        majority = n / 3
        counts = {num: nums.count(num) for num in set(nums)}

        max_nums = [num for num, count in counts.items() if count > majority]
        return max_nums


if __name__ == '__main__':
    array = [3, 2, 3]
    solution = Solution()
    print(solution.majorityElement(array))
    array = [1]
    print(solution.majorityElement(array))
    array = [1, 2]
    print(solution.majorityElement(array))
    array = [1, 2, 3, 4]
    print(solution.majorityElement(array))
    array = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    print(solution.majorityElement(array))
    array = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
    print(solution.majorityElement(array))
