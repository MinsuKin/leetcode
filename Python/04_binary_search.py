#1> Return Index Where Sum Of RHS equals to LHS in given Array
#2> LHLH or HLHL pattern , Balance it in the way require minimum Changes and Return changes Count
#3> return the count (Sorry I forget the question)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pl = 0
        pr = len(nums) - 1
        mid = pr // 2
        while pr >= pl:
            if nums[mid] > target:
                pr = mid - 1
                mid = pl + ((pr - pl) // 2)
            elif nums[mid] < target:
                pl = mid + 1
                mid = pl + ((pr - pl) // 2)
            elif nums[mid] == target:
                return mid
        return -1
