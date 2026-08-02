class Solution:
    def minWindow(self, s: str, t: str) -> str:

        count1={}
        for i in t:
            count1[i]=1+count1.get(i,0)

        res=[]
        for i in range(len(s)):
            temp_str,count2,matches='',{},0
            for j in range(i,len(s)):
                if s[i] not in count1:
                    break
                else:
                    count2[s[j]]=1+count2.get(s[j],0)
                    temp_str+=s[j]
                    if count2[s[j]]==count1.get(s[j],0):
                        matches+=1
                if matches==len(count1):
                    res.append(temp_str)
                    break
        return min(res,key=len) if len(res)>0 else ''
        