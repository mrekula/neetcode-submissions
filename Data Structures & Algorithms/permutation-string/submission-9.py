class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        if len(s2) < len(s1):
            return False
        counter_s1 =[0]*26
        counter_s2 =[0]*26
        for i in range(len(s1)):
            counter_s1[ord(s1[i])- ord('a')] += 1
            counter_s2[ord(s2[i])- ord('a')] += 1

        if counter_s1 == counter_s2:
            return True
        for r in range(len(s1), len(s2)):
            counter_s2[ord(s2[r])-ord('a')] += 1
            counter_s2[ord(s2[r-len(s1)])-ord('a')] -= 1
            if counter_s1 == counter_s2:
                return True
        
        return False


        

        









        