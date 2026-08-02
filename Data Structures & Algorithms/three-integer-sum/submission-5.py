class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        out =set()

        for i in range(len(nums)-2):
            seen_dict ={}
            target = -nums[i]
            for j in range(i+1, len(nums)):
                if target- nums[j] in seen_dict:
                    out.add(tuple(sorted([nums[i], target- nums[j], nums[j]])))
                seen_dict[nums[j]] = j
        res=[]
        for i in out:
            res.append(list(i))
        return res