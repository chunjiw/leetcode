# 57. Insert Interval
# DescriptionHintsSubmissionsDiscussSolution
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        
        result = []
        inserted = False
        for interval in intervals:
            if not inserted and interval.start >= newInterval.start:
                self.append(result, newInterval)
                inserted = True
            if not inserted:
                result.append(interval)
            else:
                self.append(result, interval)
        if not inserted:
            self.append(result, newInterval)
        return result
    
    def append(self, result, newInterval):
        if not result:
            result.append(newInterval)
        else:
            if newInterval.end <= result[-1].end:
                return
            if newInterval.start <= result[-1].end:
                result[-1].end = max(result[-1].end, newInterval.end)
            else:
                result.append(newInterval)
