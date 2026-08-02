class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False
        l, r=0,0
        s1_dict =[0]*26
        s2_dict =[0]*26
        for char in s1:
            s1_dict[ord(char)-ord('a')] += 1

        while r < len(s2):
            while r-l+1 <=len(s1):
                s2_dict[ord(s2[r])-ord('a')] += 1
                r += 1
            if s2_dict == s1_dict:
                return True
            else:
                s2_dict[ord(s2[l])-ord('a')] -= 1
                l +=1
        return False

            


        





