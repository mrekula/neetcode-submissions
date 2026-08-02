class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        og_dict={}
        for i in s1:
            og_dict[i]=1+og_dict.get(i,0)

        for i in range(len(s2)):
            count2,curr={},0
            for j in range(i,len(s2)):
                count2[s2[j]]=1+count2.get(s2[j],0)
                if (s2[j] not in og_dict) or  (count2.get(s2[j],0) > og_dict[s2[j]]):
                    break
                if  count2==og_dict:
                    return True
        return False
            