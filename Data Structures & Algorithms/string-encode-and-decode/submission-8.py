class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_out =''

        #strs = ["Hello","World"]

        for word in strs:
            encoded_out += str(len(word)) + '#'  + word
        return encoded_out
        




    def decode(self, s: str) -> List[str]:

        #'12#3ihr3lrk,lsndc'
        # '12#a2#ab'
        start = 0
        end = 0
        res =[]

        while end < len(s):
            while s[end] != '#':
                end += 1
            number = int(s[start: end])
            start = end +1
            word = s[start : start + number]
            res.append(word)
            start, end = start + number,start + number
        return res

                






