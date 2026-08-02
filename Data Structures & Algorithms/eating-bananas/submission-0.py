import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        def hours(speed):
            return sum([math.ceil(i/speed) for i in piles])



        left, right=1 , max(piles)

        while left < right:
            mid = (left+ right)//2
            if hours(mid) > h:
                left= mid+1
            elif hours(mid) <= h:
                right= mid
        return right