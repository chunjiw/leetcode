class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # invariant: last of result is disjoint with both newInterval and next interval in intervals
        # when insert to result, if newInteval and next interval are disjoint then insert smaller one
        # if newInteval and next interval overlap, merge to newInterval, and continue
        res = []
        inserted = False
        for interval in intervals:
            if inserted:
                res.append(interval)
            elif newInterval[1] < interval[0]:
                res.append(newInterval)
                res.append(interval)
                inserted = True
            elif interval[1] < newInterval[0]:
                res.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        if not inserted:
            res.append(newInterval)
        return res