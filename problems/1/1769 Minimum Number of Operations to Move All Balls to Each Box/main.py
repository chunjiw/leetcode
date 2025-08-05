class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        nums = list(map(int, boxes))
        n = len(boxes)
        balls_left = nums.copy()
        balls_right = nums.copy()
        ops_left = [0] * n
        ops_right = [0] * n
        for i in range(1, n):
            balls_left[i] += balls_left[i-1]
            ops_left[i] += ops_left[i-1] + balls_left[i-1]
        for i in range(n-2, -1, -1):
            balls_right[i] += balls_right[i+1]
            ops_right[i] += ops_right[i+1] + balls_right[i+1]    
        return [ops_left[i] + ops_right[i] for i in range(n)]