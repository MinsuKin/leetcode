# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        mid = n // 2
        pl = 1
        pr = n
        while True:
            if isBadVersion(mid) == False:
                pl = mid + 1
                mid = pl + ((pr - pl) // 2)
            elif isBadVersion(mid) == True:
                if isBadVersion(mid - 1) == False:
                    return mid
                pr = mid - 1
                mid = pr // 2
            if pl > pr:
                break
        return -1