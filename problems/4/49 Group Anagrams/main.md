
## Time Complexity

$n$ is number of strings; $m$ is number of letters in string

Use sorted string as key of a hash map: 

$$ O(nm\log(m)) $$

Use helper function `anagram(str1, str2)`:

$$ O(n^2m) $$

