class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r  = 0, len(numbers)-1

        while l < r:
            val_sum = numbers[l]+ numbers[r]
            if val_sum == target:
                return [l+1, r+1]
            elif val_sum < target:
                l += 1
            else:
                r -= 1




