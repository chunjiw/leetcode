# Confusion around what dp really is

In the editorial solution it is said
> Let `dp[i]` be the probability of having exactly `i` points at some moment.

I think this is a missing piece in the thought process of a lot of people.
First of all, we don't have `sum(dp) == 1`, because `dp[i]` is $\sum_m p_m(i)$ for all moment $m$; for $p(i)$ to normalize for all $i$, we need to fix $m$, e.g.

$$ 
\sum_ip_m(i) = 1 
$$

for any fixed $m$.

Can we make it clearer? At what moment(s) exactly, is `dp[i]` the probability of having `i` points? The anwser is

> `dp[i]` is the probability of having `i` points under the following stop rule: game stops when we get `i` or more points.

For example (let `p == 1/maxPts`): 
- For `i == 0`, the game stops without drawing any card, and the probability of having 0 point is 1. So `dp[0] = 1`
- For `i == 1`, the game stops after one draw, and the probability of having 1 point is `p`. So `dp[1] = p`
- For `i < k`, `dp[i] = sum(dp[i-j] for j in range(i-maxPts, i))`

But for this problem, we need to update the defition for `i >= k`:

> `dp[i]` is the probability of having `i` points under the following stop rule: game stops when we get `i` or more points; but before the last draw, the points cannot reach `k`

So for `i >= k`,

- `dp[i] = sum(dp[i-j] for j in range(i-maxPts, i) and i-j < k)`
