class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        timings = sorted([(p, (target-p)/s) for p,s in zip(position, speed)], reverse=True)

        max_time = 0
        fleet = 0

        for p,t in timings:
            if t > max_time:
                max_time = t
                fleet += 1
        return fleet






        