class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pl = 0
        pr = len(nums) - 1
        mid = pr // 2
        
        if target > nums[pr] or target < nums[pl]:
            return -1
        
        while pl <= pr:
            if nums[mid] < target:
                pl = mid + 1
                mid = pl + ((pr - pl) // 2)
            elif nums[mid] > target:
                pr = mid - 1
                mid = pl + ((pr - pl) // 2)
            elif nums[mid] == target:
                return mid
            
        return -1