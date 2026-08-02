class Solution:
    def search(self, nums: List[int], target: int) -> int:
        out = -1

        l, r = -1, len(nums)

        while r-l > 1:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid
            else:
                r = mid
        return out

        