class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums=sorted(nums)
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True 
        # return False

        hashset={}
        for i in nums:
            if i not in hashset:
                hashset[i]=1
            else:
                return True
        return False


        