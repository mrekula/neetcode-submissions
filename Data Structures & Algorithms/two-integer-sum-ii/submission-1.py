class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dict=collections.defaultdict(int)
        for i in range(len(numbers)):
            tmp=target-numbers[i]
            if tmp in num_dict:
                return[num_dict[tmp],i+1]
            num_dict[numbers[i]]=i+1
        return []

