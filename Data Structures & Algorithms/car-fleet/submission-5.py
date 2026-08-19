class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        fleet  = 0
        stats =[(p,s) for p, s in zip(position, speed)]
        stats.sort(reverse = True)

        max_time = float('-inf')

        for pos, speed in stats:
            time = (target - pos) / speed
            if time > max_time:
                fleet += 1
                max_time = time
        return fleet




        