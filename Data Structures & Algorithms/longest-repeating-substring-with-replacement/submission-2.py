class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # res=0

        # for i in range(len(s)):
        #     count, temp={}, 0
        #     for j in range(i, len(s)):
        #         count[s[j]] = 1+ count.get(s[j],0)
        #         if (j-i+1- max(count.values())) <=k:
        #             temp +=1
        #             res= max(res, temp)
        #         else:
        #             break
        # return res

        l=0
        res=0
        count={}

        for r in range(len(s)):
            count[s[r]]= 1+ count.get(s[r],0)
            maxf= max(count.values())
            if ((r-l+1)- maxf) > k:
                count[s[l]] -= 1
                l += 1
            else:
                res= max(res, r-l+1)
        return res
            

        