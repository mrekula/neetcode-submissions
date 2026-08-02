class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #1 .return sorted(s) == sorted(t)-- o(nlogn)

        d_s = {}
        for letter in s:
            if letter in d_s:
                d_s[letter] += 1
            else:
                d_s[letter]=0
        d_t = {}
        for letter in t:
            if letter in d_t:
                d_t[letter] += 1
            else:
                d_t[letter]=0
        return d_s == d_t
        
            

        