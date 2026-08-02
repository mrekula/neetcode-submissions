class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        count_dict={}
        for i in nums:
            count_dict[i] = 1+ count_dict.get(i,0)
        return len(count_dict) !=len(nums)


        