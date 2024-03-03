class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n>0 and 3**19%n==0

# # My code
# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         multi = 3
#         if n == 1 or n == 3:
#             return True
#         while n > multi:
#             if n / multi == 3:
#                 return True
#             multi *= 3
#         return False