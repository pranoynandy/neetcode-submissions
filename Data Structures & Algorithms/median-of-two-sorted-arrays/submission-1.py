class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = (len(nums1) + len(nums2)) // 2
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1

        l,r = 0, len(nums1)-1
        while True:
            m1 = l + (r-l)//2
            m2 = x - m1 -2

            Aleft = nums1[m1] if m1 >= 0 else float("-infinity")
            Aright = nums1[m1+1] if (m1+1) < len(nums1) else float("infinity")
            Bleft = nums2[m2] if m2 >= 0 else float("-infinity")
            Bright = nums2[m2+1] if m2+1 < len(nums2) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if (len(nums1) + len(nums2)) % 2:
                    return float(min(Aright,Bright))
                else:
                    return float((max(Aleft,Bleft) + min(Aright,Bright))/2)
                    
            elif Aleft > Bright:
                r = m1-1
            else:
                l = m1+1
            
                