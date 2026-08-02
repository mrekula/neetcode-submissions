class Solution:

    def encode(self, strs: List[str]) -> str:

        e_out = []
        for i in strs:
            e_out.append(str(len(i)))
            e_out.append('#')
            e_out.append(i)
        return ''.join(e_out)

    def decode(self, s: str) -> List[str]:

        ##.  '12#3ihr3lrk,lsndc'
        # '1#a2#ab'
        i = 0
        out =[]

        while i < len(s):
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            lag = int(s[i:j])
            out.append(s[j+1:j+1+lag])
            i = j+1+lag
        return out




