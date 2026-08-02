class Solution:

    def encode(self, strs: List[str]) -> str:
        out_list=[]

        for s in strs:
            out_list.append(str(len(s)))
            out_list.append('#')
            out_list.append(s)
        return ''.join(out_list)


    def decode(self, s: str) -> List[str]:
        i=0
        out=[]
        while i < len(s):  
            j =i
            while s[j] !='#':
                j += 1
            

            length= int(s[i:j])
            temp_word=s[j+1:j+length+1]
            out.append(temp_word)
            i = j+ length +1
        return out






