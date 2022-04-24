# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         for i in range(0, len(nums)):
#             nums[i] = nums[i] * nums[i]
#         return sorted(nums)

# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         res = []
#         l = 0
#         r = len(nums) - 1
        
#         while l <= r:
#             lvalue = nums[l] * nums[l]
#             rvalue = nums[r] * nums[r]
#             if l == r:
#                 res.insert(0, lvalue)
#                 l += 1
#             elif lvalue > rvalue:
#                 res.insert(0, lvalue)
#                 l += 1
#             elif lvalue < rvalue:
#                 res.insert(0, rvalue)
#                 r -= 1
#             elif lvalue == rvalue:
#                 res.insert(0, lvalue)
#                 res.insert(0, rvalue)
#                 l += 1
#                 r -= 1  
#         return (res)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        l, r = 0, len(nums) - 1
        
        while l <= r:
            if nums[l] * nums[l] > nums[r] * nums[r]:
                res.append(nums[l] * nums[l])
                l += 1
            else:
                res.append(nums[r] * nums[r])
                r -= 1
                
        return res[::-1]