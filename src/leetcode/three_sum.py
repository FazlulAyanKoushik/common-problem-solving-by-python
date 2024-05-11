"""
LeetCode: 3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Notice that the solution set must not contain duplicate triplets.
"""

my_list = [5, 4, -4, -3, -5, 3, 2, 1, 1, 2]

unique_list = set(my_list)

sorted_list = sorted(unique_list)

length = len(sorted_list)


def three_sum(nums):
    """
    Find all unique triplets in the array which gives the sum of zero
    """
    found = False
    for i in range(length - 2):
        l = i + 1
        r = length - 1

        while l < r:
            if sorted_list[i] + sorted_list[l] + sorted_list[r] == 0:
                print(f"Triplets: {sorted_list[i]} + {sorted_list[l]} + {sorted_list[r]} = ",
                      sorted_list[i] + sorted_list[l] + sorted_list[r])
                found = True
                break
            elif sorted_list[i] + sorted_list[l] + sorted_list[r] < 0:
                l += 1
            else:
                r -= 1

        if found:
            break

    if not found:
        print("No triplets found")


three_sum(sorted_list)


