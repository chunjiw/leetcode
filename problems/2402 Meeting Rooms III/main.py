from typing import List
from sortedcontainers import SortedList

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(reverse=True)
        empty_rooms = SortedList(range(n), key=lambda x:-x)
        occupied_rooms = SortedList(key=lambda x:(-x[0], -x[1]))    # (end time, room number)
        record = [0] * n
        time = 0
        # print(empty_rooms)
        # print(occupied_rooms)
        while meetings:
            start, end = meetings.pop()
            # print(start, end)
            # first, release rooms with finished meetings
            if time <= start:
                time = start
                while occupied_rooms and occupied_rooms[-1][0] <= time:
                    _, room = occupied_rooms.pop()
                    empty_rooms.add(room)
            if not empty_rooms:
                # wait for next available room
                time = occupied_rooms[-1][0]
                while occupied_rooms and occupied_rooms[-1][0] == time:
                    _, room = occupied_rooms.pop()
                    empty_rooms.add(room)

            # use available room to host meeting if possible
            duration = end - start
            room = empty_rooms.pop()
            occupied_rooms.add((time + duration, room))
            record[room] += 1

            # print(empty_rooms)
            # print(occupied_rooms)
        return record.index(max(record))

sol = Solution()
print(sol.mostBooked(2, [[0,10],[1,5],[2,7],[3,4]]))
print(sol.mostBooked(3, [[1,20],[2,10],[3,5],[4,9],[6,8]]))