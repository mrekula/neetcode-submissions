class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res =[]

        def dfs(subset, i):
            if i > len(nums):
                return
            if i == len(nums):
                res.append(subset.copy())
                return
            for j in range(len(nums)):
                if subset[j] is not None:
                    continue
                subset[j] = nums[i]
                print(subset)
                dfs(subset,i+1)
                subset[j] = None
        dfs([None]*len(nums),0)
        return res
            




        