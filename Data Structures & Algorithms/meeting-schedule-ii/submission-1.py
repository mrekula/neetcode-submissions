"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        time_stamps = []

        for interval in intervals:
            time_stamps.append([interval.start, 1])
            time_stamps.append([interval.end, -1])
        time_stamps.sort(key = lambda x: (x[0], x[1]))

        res = 0
        count = 0

        for i in time_stamps:
            count += i[1]
            res = max(res, count)
        return res





        


        
        