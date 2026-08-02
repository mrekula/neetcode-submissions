class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=set()
        nums = sorted(nums)
        for i in range(len(nums)-2):
            if i >0 and nums[i]==nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] == -nums[i]:
                    res.add(tuple(sorted([nums[i], nums[l], nums[r]])))
                    l += 1
                    r -= 1
                while l < r and  nums[l] + nums[r] > -nums[i]:
                    r -= 1
                while l < r and nums[l] + nums[r] < -nums[i]:
                    l += 1
        return [list(i) for i in res]
