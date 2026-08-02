class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums= set(nums)

        i =0
        out = 0

        for number in nums:
            if number -1 in nums:
                continue
            else:
                temp =1
                while number+ 1 in nums:
                    temp += 1
                    number += 1
                out = max(out, temp)

        return out
            

