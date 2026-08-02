class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        for i in range(len(s)):
            count_set, temp={},0
            for j in range(i,len(s)):
                # print(count_set)
                count_set[s[j]]=1+count_set.get(s[j],0)
                if sum(count_set.values())-max(count_set.values()) <= k:
                    temp+=1
            res=max(res, temp)
        return res

        