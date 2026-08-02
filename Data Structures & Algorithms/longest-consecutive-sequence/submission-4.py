class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        hashset = set(nums)

        res = 1
        for i in hashset:
            if i-1 not in hashset:
                temp_len = 1
                while i + 1 in hashset:
                    temp_len += 1
                    res = max(res, temp_len)
                    i = i+ 1
        
        return res






            






        