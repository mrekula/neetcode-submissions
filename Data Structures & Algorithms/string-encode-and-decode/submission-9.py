class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''

        for word in strs:
            res += str(len(word)) + '#' + word
        return res



    def decode(self, s: str) -> List[str]:
        res = []

        #'12#3ihr3lrk,lsndc'
        # '12#a2#ab'
        start, end = 0,0

        while end < len(s):
            while end < len(s) and s[end] != '#':
                end += 1
            word_len = int(s[start:end])
            start = end + 1
            res.append(s[start : start+ word_len])
            start = end = start + word_len
        return res
            
            


                






