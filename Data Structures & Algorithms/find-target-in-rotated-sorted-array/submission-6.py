class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # l =0
        # r = len(nums)-1

        # while  l <= r:
        #     mid = (l+r)//2
        #     if nums[mid]==target:
        #         return mid
        #     # its on left sorted array
        #     if nums[mid] >= nums[l]:
        #         if nums[l] <= target < nums[mid]:
        #             r= mid-1
        #         else:
        #             l = mid+1
        #     # its on the right sorted array
        #     else:
        #         if nums[mid] < target <= nums[r]:
        #             l = mid+1
        #         else:
        #             r= mid-1
        # return -1

        lo, hi = 0, len(nums) - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2

            # Case 1: nums[mid] and target are on the same side of rotation
            if (nums[mid] >= nums[0]) == (target >= nums[0]):
                mid_val = nums[mid]   # safe to compare normally

            # Case 2: They are on different sides
            else:
                # If target is in left part, map nums[mid] on right part to +inf
                if target >= nums[0]:
                    mid_val = float('inf')
                # If target is in right part, map nums[mid] on left part to -inf
                else:
                    mid_val = float('-inf')

            if mid_val < target:
                lo = mid + 1
            elif mid_val > target:
                hi = mid - 1
            else:
                return mid

        return -1





        