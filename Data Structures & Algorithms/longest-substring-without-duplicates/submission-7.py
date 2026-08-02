class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen_dict ={}

        l, r =0, 0
        max_len=0

        while r in range(0, len(s)):
            if s[r] in seen_dict and seen_dict[s[r]] >= l:
                l = seen_dict[s[r]]+1
            
            max_len  = max(max_len, r-l+1)
            seen_dict[s[r]] =r
            r += 1
        return max_len



        