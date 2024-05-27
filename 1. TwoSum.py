from typing import List

'''Solution using dictionary: store each element with its index, check for the difference,
if differnce is there, return the index of element and the current element.
Time Complexity: O(n), because we only loop through the dictionary one time.
Space Complexity: O(n), because in the worst case we will store the whole dictionary.'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappings = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in mappings:
                return [mappings[complement], i]
            mappings[nums[i]]=i




# Solution using two pointers
# Time Complexity: O(nlogn), because of the sorting (TimeSort in python)
# Space Complexity: O(n), additional space to store the original indices

# original_order = [(num,i) for i, num in enumerate(arr)]
# original_order.sort()
# print(original_order)
# left = 0
# right = len(original_order)-1
# while left < right:
#     left_num, left_idx = original_order[left]
#     right_num, right_idx = original_order[right]
#     current_sum = left_num + right_num

#     if current_sum == target:
#         return [left_idx, right_idx]
#     elif current_sum < target:
#         left +=1
#     else:
#         right-=1


# Brute Force solution to the problem, seeing every possible combination of the pair of numbers that sum up to the target
# Time Complexity: O(n^2), Space Complexity: O(n)

# arr=list(map(int,input().split()))
# target = int(input())
# for i in range(len(arr)-1):
#     for j in range(1,len(arr)):
#         if arr[i]+arr[j]==target:
#             return [i,j]




