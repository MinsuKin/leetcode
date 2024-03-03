
# Neetcode - HashMap, TC = O(n), SC = O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevMap = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i



# # My code - Brute force, TC = O(n^2), SC = O(1)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         i = 0
#         for i in range(i, len(nums)):
#             j = i + 1
#             for j in range(j, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]