class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # - nums[i]= nums[j]+nums[k]


        res=set()
        for i in range(len(nums)-1):
            out = {}
            target = -nums[i]
            for j in range(i+1, len(nums)):
                if target-nums[j] in out:
                    res.add(tuple(sorted(([nums[i],nums[j],target-nums[j]]))))
                else:
                    out[nums[j]]= j
        return [i for i in res]