class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = 1
        res =[1] * len(nums)
        for i, num in enumerate(nums):
            res[i] = prefix
            prefix *= num

        suffix = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] *= suffix
            suffix *= nums[j]
        return res
        
        


        