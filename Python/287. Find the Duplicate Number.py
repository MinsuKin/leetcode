class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        nums.sort()
        for i in range(1, length):
            if nums[i] == nums[i-1]:
                return nums[i]