<!-- Title: Thought Process to Optimal Solution -->

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

At each location, the count of water trapped depends on the highest bar to the left `lmax`, and the highest bar to the right `rmax`. To be more precise, it depends on `min(lmax, rmax)`, because the lowest boundary determines water level. But how do we get `lmax` and `rmax`, as they will change with location?

The trick is that you don't need to know both `lmax` and `rmax`; you just need to know the lower value of the two. Here comes an important observation: going from left to right, `lmax` must be monotonically increasing; similarly, from right to left, `rmax` is also increasing.

So, given two index, `left` and `right`, and their corresponding `lmax[left]` and `rmax[right]`, assume `lmax[left] < rmax[right]`, then we are sure, `lmax[left] < rmax[right] < rmax[left]`.

We know `lmax[0] = 0` and `rmax[n-1] = 0`, so we can start from both ends and work towards the middle.

# Approach
<!-- Describe your approach to solving the problem. -->

For a pair of indices `left` and `right`, calculate the water at one of them, then move it to the middle. Keep updating `lmax` and `rmax` along the way.

# Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(1)$$

# Code
```python3 []
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        lmax, rmax = 0, 0
        water = 0
        while left <= right:
            if lmax <= rmax:
                if lmax >= height[left]:
                    water += lmax - height[left]
                else:
                    lmax = height[left]
                left += 1
            else:
                if rmax >= height[right]:
                    water += rmax - height[right]
                else:
                    rmax = height[right]
                right -= 1
        return water
```