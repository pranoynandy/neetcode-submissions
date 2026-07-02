class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l,r = 0, mountainArr.length()-1
        while l<=r:
            m = l+(r-l)//2
            if mountainArr.get(m-1) < mountainArr.get(m) < mountainArr.get(m+1):
                l = m+1
            elif mountainArr.get(m-1) > mountainArr.get(m) > mountainArr.get(m+1):
                r = m-1
            else:
                break
        peak = m


        l,r = 0,peak
        while l<=r:
            m = l + (r-l)//2
            if mountainArr.get(m) > target:
                r = m-1
            elif mountainArr.get(m) < target:
                l = m+1
            else:
                return m


        l,r = peak+1, mountainArr.length()-1
        while l<=r:
            m = l + (r-l)//2
            if mountainArr.get(m) < target:
                r = m-1
            elif mountainArr.get(m) > target:
                l = m+1
            else:
                return m


        return -1
        