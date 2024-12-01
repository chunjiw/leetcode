<!-- Title: Proof of Correctness -->

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

If we already know we should use two pointers to avoid $O(n^2)$ complexity, then we need to find a rule to know how to move two pointers.

First, we cannot expect to have the next container always larger (or smaller) than the current one. Both are possible. Which means we need to keep track of optimal solution along the way.

Then we think about the optimal solution itself. Assume $(i^*, j^*)$ is the solution. Then we have

$$  h[k] < h[j^*] \text{ for all } k < i^*  $$

$$  h[l] < h[i^*] \text{ for all } l > j^*  $$

At this point we can boldly try to move the index with lower height.

# Proof

However, it is not immediately obvious that we won't miss the optimal solution. At least not to me. To prove it by contradiction:

If we missed the optimal solution $(i^*, j^*)$, then at some point, we passed through one of them without passing the other. Assume we passed $i^*$ at $l>j^*$; according to our rule, $h[i^*] \le h[l]$. But this is in contradiction with our previous observation.

Without explicitly writing this proof out, I find it difficult to intuitively know it for sure.