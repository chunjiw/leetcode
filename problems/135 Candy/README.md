<!-- Title: Thought Process to Optimal Solution -->

# Intuition

Relax the requirements; simplify conditions; break the problem into smaller ones. Gather insights then add them up.

## At Least One vs At Least Zero

First requirement says:

> Each child must have at least one candy.

But what if each child must have at least zero candy? We can distribute one candy to each child at the end.

## Equal Ratings

Second requirement says:

> Children with a higher rating get more candies than their neighbors.

It does not say anything when ratings are equal. That means no requirements. so when two neighbor children have equal ratings, we can treat the second child as the start of another independent line of children. In another word, we can re-initialize all conditions and start new.

## Increasing vs Decreasing Ratings

What if ratings are increasing all the way up? We just need to start from zero and increment candies as we go:

```
ratings: 3 4 5 6 7
candies: 0 1 2 3 4
```

So we keep a variable `up` and increment it along the way, and add it to `result`.

What if ratings are decreasing all the way down? We can also start from zero, but we need to compensate candies to previous children as we go:

```
steps   ratings: 7 6 5 4 3   result
  0     candies: 0             +0
  1     candies: 1 0           +1
  2     candies: 2 1 0         +2
  3     candies: 3 2 1 0       +3
  4     candies: 4 3 2 1 0     +4
```

So, similar as before, we keep a variable `down` and increment it along the way, and add it to `result`.

## Increasing then Decreasing Ratings

This is the only difficult part. We can just try our previous intuitions and see how it goes:

```
steps   ratings: 5 6 5 4   up   down   result
  0     candies: 0          0     0      +0
  1     candies: 0 1        1     0      +1
  2     candies: 0 1 ?      0     1       ?
```

At step 2, `down` variable should be 1, but no need to compensate previous child since they already got 1 candy. Which means we don't need to compensate. Let's keep going:

```
steps   ratings: 5 6 5 4   up   down   result
  0     candies: 0          0     0      +0
  1     candies: 0 1        1     0      +1
  2     candies: 0 1 0      0     1      +0
  3     candies: 0 1 0 ?    0     2       ?
```

At step 3, `down` variable is 2, it seems we need to compensate in this case:

```
        index:   0 1 2 3
steps   ratings: 5 6 5 4   up   down   result
  2     candies: 0 1 0      0     1      +0
  3     candies: 0 2 1 0    0     2      +2
```

Why we need to compensate child 1 at step 3, but not at step 2? That's because at step 2, child 1 value (`peak`) is bigger or equal to `down`, so we don't need to compensate. In another word, if `down` is not big enough yet, we need to adjust the rules we get from previous intuitions.

That's it!

# Approach

- Initialize four variables `up`, `down`, `peak`, `res` as zeroes;
- if ratings are up, increment `up` and add to `res`; 
- if ratings are down, increment `down` and add to `res`, but if `down` is not bigger than `peak`, decrement `result`;
- set or reset `up`, `down`, `peak` when appropriate;
- don't forget to add `len(ratings)` in the end.

# Complexity
- Time complexity:
$$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
$$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        prev = ratings[0]
        up, down, peak, res = 0, 0, 0, 0
        for curr in ratings[1:]:
            if prev == curr:
                up, down, peak = 0, 0, 0
            elif prev < curr:
                up += 1
                peak = up
                res += up
                down = 0
            else:
                down += 1
                res += down
                if down <= peak:
                    res -= 1
                up = 0
            prev = curr
        return res + len(ratings)
```