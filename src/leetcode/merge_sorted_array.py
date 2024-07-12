"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function,
but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n,
where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
"""

# Approach:
# 1. Start from the end of the two arrays.
# 2. Compare the last elements of both arrays and put the larger element at the end of the first array.
# 3. Decrement the index of the array which had the larger element.
# 4. Continue this process until the first array is completely filled.

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge nums1 and nums2 into a single array sorted in non-decreasing order
        """
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


if __name__ == '__main__':
    s = Solution()
    nums_1 = [1, 2, 3, 4, 0, 0, 0]
    m = 4
    nums_2 = [2, 5, 6]
    n = 3
    s.merge(nums_1, m, nums_2, n)
    print(nums_1)