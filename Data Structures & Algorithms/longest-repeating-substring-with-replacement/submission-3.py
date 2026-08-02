class Solution:
    def characterReplacement(self, s: str, k: int) -> int:



        res=0
        for i in range(len(s)):
            counter, maxf ={}, 0
            for j in range(i, len(s)):
                counter[s[j]] = 1+counter.get(s[j],0)
                maxf = max(maxf,counter[s[j]] )
                if j-i+1 - maxf <=k:
                    res = max(res, j-i+1)
                else:
                    break
        return res




        

        