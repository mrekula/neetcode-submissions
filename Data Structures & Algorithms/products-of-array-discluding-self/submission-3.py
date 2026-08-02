class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # having one/more zero cases
        # one zero

        # final_prod= 1
        # count =0
        # for num in nums:
        #     if num !=0:
        #         final_prod *= num
        #     else:
        #         count += 1
        # if count ==0:
        #     return [final_prod//num for num in nums]
        # elif count > 1:
        #     return [0]*len(nums)
        # else:
        #     return [final_prod if num==0 else 0 for num in nums]


    ## Prefix and suffix method

        prefix_out =[1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            prefix_out[i] = prefix
            prefix *= nums[i]
        suffix =1
        for j in range(len(nums)-1, -1, -1):
            prefix_out[j] *= suffix
            suffix *= nums[j]
        return prefix_out
        

        