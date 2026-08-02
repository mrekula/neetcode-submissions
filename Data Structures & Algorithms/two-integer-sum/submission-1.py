class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # for i in range(0,len(nums)):
        #     for j in range(i,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        sum_dict={}
        for i in range(len(nums)):
            if target-nums[i] in sum_dict:
                return [sum_dict[target-nums[i]],i]
            else:
                sum_dict[nums[i]]=i

