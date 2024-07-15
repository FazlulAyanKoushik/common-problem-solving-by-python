"""169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times.
You may assume that the majority element always exists in the array.

Example 1:
    Input: [3,2,3]
    Output: 3

Example 2:
    Input: [2,2,1,1,1,2,2]
    Output: 2

Constraints:
    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)
        majority = n / 2
        counts = {num: nums.count(num) for num in set(nums)}

        max_num = [num for num, count in counts.items() if count > majority]
        return max_num[0]


if __name__ == '__main__':
    # array = [3, 2, 3]
    array = [2, 2, 1, 1, 1, 2, 2]
    solution = Solution()
    print(solution.majorityElement(array))
