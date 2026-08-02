class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # l, r =0,0
        # out ={}
        # leng = 0

        # while r < len(s):
        #     out[s[r]] = 1+ out.get(s[r],0)
        #     while r-l+1 -max(out.values()) > k:
        #         out[s[l]] -= 1
        #         print(r,l)
        #         l += 1
        #     leng = max(leng, r-l+1)
        #     r += 1
        # return leng

        res =0 
        for i in range(len(s)):
            count_f={}
            maxf= 0
            for j in range(i, len(s)):
                count_f[s[j]] = 1+ count_f.get(s[j], 0)
                maxf = max(maxf,count_f[s[j]] )
                if j-i+ 1 - maxf <= k:
                    res = max(res, j-i+1)
                else:
                    break
        return res

