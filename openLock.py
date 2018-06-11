# 752. Open the Lock
# DescriptionHintsSubmissionsDiscussSolution
# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

# The lock initially starts at '0000', a string representing the state of the 4 wheels.

# You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

# Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

# Example 1:
# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6
# Explanation:
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
# because the wheels of the lock become stuck after the display becomes the dead end "0102".
# Example 2:
# Input: deadends = ["8888"], target = "0009"
# Output: 1
# Explanation:
# We can turn the last wheel in reverse to move from "0000" -> "0009".
# Example 3:
# Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
# Output: -1
# Explanation:
# We can't reach the target without getting stuck.
# Example 4:
# Input: deadends = ["0000"], target = "8888"
# Output: -1


class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if target == "0000":
            return 0
        stophere = set(deadends)
        step = 0
        level = ["0000"]
        while level:
            newlevel = []
            step += 1
            for node in level:
                if node not in stophere:
                    stophere.add(node)
                    for child in self.nextnode(node):
                        if child == target:
                            return step
                        newlevel.append(child)
            level = newlevel
        return -1
        
    def nextnode(self, node):
        result = []
        let = list(node)
        for i in range(4):
            for digit in self.neighbor(node[i]):
                let[i] = digit
                result.append(''.join(let))
                let[i] = node[i]
        return result        
        
    def neighbor(self, digit):
        if digit == '0':
            return ['1', '9']
        if digit == '9':
            return ['0', '8']
        return [str(int(digit) + 1), str(int(digit) - 1)]
        
    
        
