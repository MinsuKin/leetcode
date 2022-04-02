class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        pl = 0
        pr = length - 1
        mid = pr // 2
        while True:
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                pl = mid + 1
                mid = pl + ((pr - pl) // 2)
            elif target < nums[mid]:
                pr = mid - 1
                mid = pl + ((pr - pl) // 2)
            if pl > pr:
                break
        return mid + 1