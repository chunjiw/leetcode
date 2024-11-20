# 293. Flip Game
# DescriptionHintsSubmissionsDiscussSolution
# You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

# Write a function to compute all possible states of the string after one valid move.

# Example:

# Input: s = "++++"
# Output: 
# [
#   "--++",
#   "+--+",
#   "++--"
# ]
# Note: If there is no valid move, return an empty list [].


class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or "++" not in s:
            return []
        
        result = []
        for i in range(0, len(s) - 1):
            if s[i:i+2] == "++":
                result.append(s[:i] + "--" + s[i+2:])
        return result
