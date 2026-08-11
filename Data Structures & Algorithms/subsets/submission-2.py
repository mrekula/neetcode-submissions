class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res =[[]]
        for num in nums:
            temp=[]
            for subset in  res:
  
                temp.append(subset + [num])
            res.extend(temp)
        return res














        # res =[]
        # def dfs(i,subset):
        #     if i > len(nums):
        #         return 
        #     if i ==len(nums):
        #         res.append(subset.copy())
        #         return 
        #     subset.append(nums[i])
        #     dfs(i+1,subset)
        #     subset.pop()
        #     dfs(i+1,subset)
        # dfs(0,[])
        # return res
   






            



        



        