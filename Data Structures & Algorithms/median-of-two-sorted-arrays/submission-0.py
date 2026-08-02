class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2 =0, 0
        out =[]

        while l1 < len(nums1) and l2 < len(nums2):
            if nums1[l1] <= nums2[l2]:
                out.append(nums1[l1])
                l1 += 1
            else:
                out.append(nums2[l2])
                l2 += 1
        out.extend(nums1[l1:])
        out.extend(nums2[l2:])

        if len(out)% 2 !=0:
            target= len(out) //2
            return out[target]
        else:
            target= len(out) //2
            return (out[target-1] + out[target]) /2

        