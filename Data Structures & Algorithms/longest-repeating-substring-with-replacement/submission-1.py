class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res=0

        for i in range(len(s)):
            count, temp={}, 0
            for j in range(i, len(s)):
                count[s[j]] = 1+ count.get(s[j],0)
                if (sum(count.values())- max(count.values())) <=k:
                    temp +=1
                    res= max(res, temp)
                else:
                    break
        return res
            

        