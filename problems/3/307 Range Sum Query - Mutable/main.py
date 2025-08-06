# algo: segment tree
# Time C: O(log n)
# Space: O(n)

class NumArray:
    # O(n)
    def __init__(self, nums: list[int]):
        n = len(nums)
        self.tree = [0] * (4*n)
        self.n = n
        # self.nums = nums

        def recursion(node, left, right):
            if left == right:
                self.tree[node] = nums[left]
            else:
                mid = (left + right) // 2
                recursion(2*node, left, mid)
                recursion(2*node+1, mid+1, right)
                self.tree[node] = self.tree[2*node] + self.tree[2*node+1]

        recursion(1, 0, n-1)
    
    # O(log n)
    def update(self, index: int, val: int) -> None:
        
        def recursion(node, left, right):
            if left == right:
                self.tree[node] = val
            else:
                mid = (left + right) // 2
                if index <= mid:
                    recursion(2*node, left, mid)
                else:
                    recursion(2*node+1, mid+1, right)
                self.tree[node] = self.tree[2*node] + self.tree[2*node+1]         

        recursion(1, 0, self.n-1)    
    
    # O(log n)
    def sumRange(self, left: int, right: int) -> int:
    
        def recursion(node, l, r):
            if (l == left and r == right) or l == r:
                return self.tree[node]
            else:
                m = (l + r) // 2
                if right <= m:
                    return recursion(2*node, l, m)
                elif left > m:
                    return recursion(2*node+1, m+1, r)
                else:
                    return recursion(2*node, l, m) + recursion(2*node+1, m+1, r)

        return recursion(1, 0, self.n-1)    
    
na = NumArray([1,3,5])
print(na.tree)
print(na.sumRange(0, 2))
print(na.sumRange(0, 1))
print(na.sumRange(1, 2))
print(na.update(1,2))
print(na.tree)


