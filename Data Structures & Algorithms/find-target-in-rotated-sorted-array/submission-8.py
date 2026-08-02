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

        l, r = -1, len(nums)

        while r-l > 1:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            if (nums[mid] >= nums[0]) == (target >= nums[0]):
                mid_val = nums[mid]
            else:
                if target >= nums[0]:
                    mid_val = float('inf')
                else:
                    mid_val = float('-inf')

            if mid_val < target:
                l = mid 
            else:
                r = mid 
        return -1





        