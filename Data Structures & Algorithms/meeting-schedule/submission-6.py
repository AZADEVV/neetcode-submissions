"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # if not intervals:return False
   
        # seen = [intervals[0]]

        # for i in range(1, len(intervals)):
        #     interval = intervals[i]

        #     for see in seen:
        #         if see.start <= interval.start and see.end >= interval.end or interval.start >= see.start and interval.end < see.end:
        #             return False
    
        #     seen.append(interval)
        # return True

        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if intervals[j].start >= intervals[i].start and intervals[j].start < intervals[i].end or intervals[j].end <= intervals[i].end and intervals[j].end >= intervals[i].start:
                    return False

        return True