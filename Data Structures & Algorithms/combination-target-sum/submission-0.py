class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        res =[]

        def dfs(i, subset):
            if sum(subset) > target:
                return
            if sum(subset) == target:
                res.append(subset.copy())
                return
            for j in range(i, len(nums)):
                if sum(subset) + nums[j] > target:
                    continue
                subset.append(nums[j])
                dfs(j, subset)
                subset.pop()
        dfs(0,[])
        return res


        