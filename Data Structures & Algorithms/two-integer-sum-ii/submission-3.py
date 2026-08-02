class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        char_dict={}

        for i,num in enumerate(numbers):
            if target-num in char_dict:
                return [char_dict[target-num], i+1]
            else:
                char_dict[num]=i+1


