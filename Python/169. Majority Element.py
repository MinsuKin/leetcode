class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # """My code"""
        # dict = {}
        
        # for i in nums:
        #     if dict.get(i):
        #         dict[i] += 1
        #     else:
        #         dict[i] = 1
        
        # return max(dict, key=dict.get)

        # """Boyer Moore - O(1) Space complexity"""
        # cnt = []
        # for i in nums:
        #     if not cnt:
        #         cnt.append(i)
        #         cnt.append(1)
        #     if cnt[0] == i:
        #         cnt[1] += 1
        #     if cnt[0] != i:
        #         cnt[1] -= 1
        #     if cnt[1] == 0:
        #         cnt[0] = i
        #         cnt[1] = 1
        # return cnt[0]
    
        """Neetcode"""
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)        
        return res