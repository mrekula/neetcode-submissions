class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        '''
        counter of window

        for r in range():
            add s[r]
            remove s[l]
            l += 1
            check if valid


        '''
        counter_s1 = Counter(s1)
        counter_s2 = Counter(s2[0: len(s1)])

        if counter_s1 == counter_s2:
            return True
        l = 0

        for r in range(len(s1), len(s2)):
            counter_s2[s2[r]] = 1 + counter_s2.get(s2[r],0)
            counter_s2[s2[l]] -= 1
            if counter_s2[s2[l]] == 0:
                del counter_s2[s2[l]]
            l += 1
            if counter_s2 == counter_s1:
                return True
        return False
            


 
        









        