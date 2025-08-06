# algo: segment tree
# Time C: O(log n)
# Space: O(n)

class NumArray:
    # O(n)
    def __init__(self, nums: list[int]):
        n = len(nums)
        self.tree = [0] * n + nums
        for i in range(n-1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
        self.n = n

    # O(log n)
    def update(self, index: int, val: int) -> None:
        i = self.n + index
        self.tree[i] = val
        i //= 2
        while i >= 1:
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
            i //= 2
        
    # O(log n)
    def sumRange(self, left: int, right: int) -> int:
        result = 0
        left += self.n
        right += self.n
        while left <= right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 0:
                result += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return result
        

na = NumArray([1,3,5])
print(na.tree)
print(na.sumRange(0, 2))
print(na.sumRange(0, 1))
print(na.sumRange(1, 2))
print(na.update(1,2))
print(na.tree)


