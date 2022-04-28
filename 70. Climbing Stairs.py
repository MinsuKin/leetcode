# # Memory Limit Exceeded
# import itertools

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         arr = [1] * n
#         res = 1
#         i = 1
#         for _ in range(n // 2):
#             arr.insert(0, 2)
#             arr.pop()
#             arr.pop()
#             noc= set(list(permutations(arr, n - i)))
#             i += 1
#             res += len(noc)
#         return res


# neetcode
class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        
        for _ in range(n - 1):
            tmp = one
            one = one + two
            two = tmp
        return one

# # 승지니어
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 1:
#             return 1
#         dp = [1] * n
#         dp[0] = 1
#         dp[1] = 2
        
#         for i in range(2, n):
#             dp[i] = dp[i-1] + dp[i-2]
#         return dp[n - 1]