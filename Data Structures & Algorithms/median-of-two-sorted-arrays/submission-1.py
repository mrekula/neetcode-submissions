class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        p1,p2 = 0,0
        out=[]
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] <= nums2[p2]:
                out.append(nums1[p1])
                p1 += 1
            else:
                out.append(nums2[p2])
                p2 += 1
        
        out.extend(nums2[p2:])
        out.extend(nums1[p1:])


        middle = len(out)//2
        if len(out) % 2!= 0:
            return out[middle]
        else:
            return (out[middle] + out[middle-1])/2
        