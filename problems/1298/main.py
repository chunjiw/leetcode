from typing import List
from collections import deque

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        obtained_keys = set()
        open_boxes = set()
        result = 0

        unlocked_boxes = deque([box for box in initialBoxes if status[box] == 1])
        locked_boxes = set([box for box in initialBoxes if status[box] == 0])
        
        while unlocked_boxes:
            box = unlocked_boxes.popleft()
            if box in open_boxes:
                continue
            open_boxes.add(box)
            result += candies[box]
            for key in keys[box]:
                obtained_keys.add(key)
                if key in locked_boxes:
                    locked_boxes.remove(key)
                    unlocked_boxes.append(key)
            for bb in containedBoxes[box]:
                if status[bb] == 1 or bb in obtained_keys:
                    unlocked_boxes.append(bb)
                else:
                    locked_boxes.add(bb)
        return result

