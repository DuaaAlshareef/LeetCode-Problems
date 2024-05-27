from typing import List
import time              


'''
Solution_1: create a set, check if element is already in the set -> duplicate.
Time Complexity: O(n), creating the set operation.
Space Complexity: O(n), creating the set requires additional space to store the elements.
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_elements = set()
        for i in nums:
            if i in unique_elements:
                return True
            unique_elements.add(i)
        return False
        



'''
We can do another implementation of the same approach:
Solution_2: using a set, convert list to set (which contains all the unique elements in the list),
if the length of the list == length of the set -> no duplicates.
Time Complexity: O(n), creating the set operation.
Space Complexity: O(n), creating the set requires additional space to store the elements.
'''


# def containsDuplicate2(nums: List[int]) -> bool:
#     return len(nums)!=len(set(nums))






'''
Solution_3: by sorting, sort then compare adjacent elements for duplicates.
Time Complexity: O(nlogn), because of the sorting operation.
Space Complexity: O(1), no extra memory used.
'''
# def containsDuplicate(self, nums: List[int]) -> bool:
  # nums.sort()
  # flag = False
  # for i in range(len(nums)-1):
  #     if nums[i] == nums[i+1]:
  #         flag = True
  # return flag



'''
Solution_4: using a dictionary to store count of each number, if number is already in the dictionary,
it is a duplicate -> return True.
Time Complexity: O(n), looping one time through the list.
Space Complexity: O(n), creating the dictionary.
'''

# def containsDuplicate(self, nums: List[int]) -> bool:
  # occurs = {}
  # flag=False
  # for i in range(len(nums)):
  #     if nums[i] in occurs:
  #       flag = True
  #     else:
  #       occurs[nums[i]]=1

  # return flag




'''
Solution_5: two for loops to go through all possible combinations of numbers, comparing for duplicates.
Time Complexity: O(n^2).
Space Complexity: O(1), did not use any extra memory space.
Time Limit Exceeded when submitting to leetcode.
'''
# def containsDuplicate(self, nums: List[int]) -> bool:
#   nums=list(map(int,input().split()))
#   flag = False
#   for i in range(len(nums)-1):
#       for j in range(1,len(nums)-1):
#           if nums[i] == nums[j]:
#               flag = True
#   return flag







'''
Comparing the timing of Solution_1 and Solution_2:
'''
# # Solution_1
# # Sample data
# nums = [7,4,6,1,1] * 10000  # Making the list large to see the performance difference

# start = time.time()
# def containsDuplicate1(nums: List[int]) -> bool:
#     unique_elements = set()
#     for i in nums:
#         if i in unique_elements:
#             return True
#         unique_elements.add(i)
#     return False


# print("containsDuplicate without len: ", containsDuplicate1(nums))
# end = time.time()
# print("Time: ", end - start)

# #Solution_2
# start = time.time()
# def containsDuplicate2(nums: List[int]) -> bool:
#     return len(nums)!=len(set(nums))

# print("containsDuplicate with len: ", containsDuplicate2(nums))
# end = time.time()
# print("Time: ", end - start)


# Output:
# containsDuplicate without len:  True
# Time:  4.506111145019531e-05
# containsDuplicate with len:  True
# Time:  0.0002791881561279297

'''
The difference in time, suggests that solution_1 may be faster in practice,
especially for lists with duplicates occurring early. 
While solution_2: needs to create a set from the entire list before comparing lengths,
which incurs additional overhead compared to the direct approach of solution_1.
'''