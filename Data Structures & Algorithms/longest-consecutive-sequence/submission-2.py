class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store=set(nums)
        max_seq_len=0
        for num in nums:
            streak,curr=0,num
            if num-1 not in store:
                while curr in store:
                    streak+=1
                    curr+=1
            max_seq_len=max(max_seq_len,streak) 
        return max_seq_len
        