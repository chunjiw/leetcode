# 253. Meeting Rooms II
DescriptionHintsSubmissionsDiscussSolution
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


from heapq import heappush, heappop

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        rooms = []
        intervals.sort(key = lambda x: x.start)
        
        for interval in intervals:
            # the earlist finished meeting room can accomodate, so new room not needed
            if rooms and rooms[0][1].end <= interval.start:
                heappop(rooms)
            heappush(rooms, (interval.end, interval))
        return len(rooms)
