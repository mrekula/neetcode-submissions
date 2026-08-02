class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seenset= set()

        l, r= 0,0
        out=0

        while r < len(s):
            if s[r] not in seenset:
                out = max(out, r-l+1)
            else:
                while s[r] in seenset:
                    seenset.remove(s[l])
                    l += 1
            seenset.add(s[r])
            r += 1
        return out

