Look for $m_1$ such that $l_1[0:m_1]$ and $l_2[0:m_2]$ together are the left half of the merged sorted array.

Define $h = \lfloor (n_1+n_2) / 2 \rfloor$, and $m_2 = h-m_1-2$ and assume $n_1 \leq n_2$

If $m_1 < n_1 - 1$, then 
$$
m_2 = h - m_1 - 2 > h - n_1-1
$$

Because $h \geq n_1$, so
$$
m_2 > h-n_1-1 \geq -1
$$
Or just
$$
m_2 > -1
$$

If $m_1 \geq 0$ then $m_2 \leq h-2 \leq n_2 - 2$.

So if $ 0 \leq m_1 < n_1 - 1$, then $ 0 \leq m_2 < n_1 - 1$.

If $m_1 = n_1 - 1$, then $m_2$ is possibly negative, we need to be careful. But then, in the binary search loop, `m` will never be $n_1 - 1$ because it would mean `i==j` so the while loop iteration already breaks.

Which means the validity test involving $l_k[m_k]$ and $l_k[m_k+1]$ for $k = 1,2$ is always OK to test.

If the loop exits without returning, there are several situations:

1. $l_1$ has only one element. Deal with this corner case in the beginning;
2. `i == 0`, which means the whole $l_1$ is at the right half of the merged array;
3. `i == n1 - 1` which means the whole $l_1$ is at the left half of the merged array.