class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

       # return len(set(nums)) != len(nums) # time and space for set creation?

        # sort and see if any neightbours are the same number
        # nums= sorted(nums) # what is sort complexity

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False # o(N) as time complexity

        # use dictionary and see if key exists
        d_ = {}
        for i in nums:
            if i in d_:
                return True
            else:
                d_[i] = 1
        return False # o(N) time and space complexity
        