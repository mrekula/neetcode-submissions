class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # char_dict={}

        # for i,num in enumerate(numbers):
        #     if target-num in char_dict:
        #         return [char_dict[target-num], i+1]
        #     else:
        #         char_dict[num]=i+1

        left, right = 0, len(numbers)-1

        while left < right:
            mysum=numbers[left]+ numbers[right]
            if mysum ==target:
                return [left+1, right+1]
            elif mysum > target:
                right -= 1
            else:
                left += 1




