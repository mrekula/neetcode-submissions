class Solution:

    def encode(self, strs: List[str]) -> str:

        final_str=''
        for i in strs:
            final_str=final_str + str(len(i))+'#' + i
        return final_str



    def decode(self, s: str) -> List[str]:
        i=0
        num=0
        res=[]

        while i < len(s):
            while s[i] != '#':
                num = num * 10 + int(s[i])
                i = i+1
            res.append(s[i+1:num+i+1])
            i += num+1
            num =0
        return res





