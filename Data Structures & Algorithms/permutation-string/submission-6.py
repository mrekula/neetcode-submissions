class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:



        if len(s1) > len(s2):
            return False        

        count_s1 ={}
        count ={}
        for letter in range(len(s1)):
            count_s1[s1[letter]] = 1+ count_s1.get(s1[letter],0)
            count[s2[letter]] = 1+ count.get(s2[letter],0)

        if count_s1 == count:
            return True

        
        for r in range(len(s1), len(s2)):
            count[s2[r]] = 1+ count.get(s2[r],0)
            left = r- len(s1)
            count[s2[left]] -= 1

            if count[s2[left]] ==0:
                del count[s2[left]]
        
            if count == count_s1:
                return True
        return False




        