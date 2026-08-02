class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers_dict=collections.defaultdict()
        for i, num in enumerate(numbers):
            numbers_dict[num]=i
        for num in numbers_dict:
            if target-num in numbers_dict:
                break
        return [numbers_dict[num]+1,numbers_dict[target-num]+1]
        