class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False

        track_s1 =[0]*26
        for s in s1:
            track_s1[ord(s)-ord('a')] += 1
        print(track_s1)

        l, r =0, 0
        track_s2 =[0]*26
        while r in range(len(s2)):
            if r-l+1 > len(s1):
                track_s2[ord(s2[r])-ord('a')] += 1
                track_s2[ord(s2[l])-ord('a')] -= 1
                l += 1

            else:
                track_s2[ord(s2[r])-ord('a')] += 1 
            if track_s2==track_s1:
                return True

            r += 1
        return False

        







        