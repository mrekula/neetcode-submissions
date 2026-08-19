class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        lookup_dict ={}

        for i, num in enumerate(nums):
            if target - num in lookup_dict:
                return [lookup_dict[target - num],i]
            lookup_dict[num] = i
        return []
            




