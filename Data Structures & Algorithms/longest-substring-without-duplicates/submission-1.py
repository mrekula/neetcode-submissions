class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l, r, maxl = 0, 1, 0

        # while r < len(s):
        #     while s[r] in s[l:r]:
        #         l += 1
        #     maxl = max(maxl, r-l+1)
        #     r += 1
        # return maxl

        for i in range(len(s)):
            seen = set()
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
                maxl = max(maxl,j-i+1 )
        return maxl

