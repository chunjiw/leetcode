1512. Number of Good Pairs

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:

Input: nums = [1,2,3]
Output: 0

Constraints:

    1 <= nums.length <= 100
    1 <= nums[i] <= 100

Hint 1
Count how many times each number appears. If a number appears n times, then n * (n – 1) // 2 good pairs can be made with this number.
Similar Questions
Number of Pairs of Interchangeable Rectangles
Medium
Substrings That Begin and End With the Same Letter
Medium
Discussion (109)
💡 Discussion Rules

1. Please don't post any solutions in this discussion.

2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.

3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.
No comments yet.
Copyright ©️ 2025 LeetCode All rights reserved
19 Online
1
2
3
Saved
nums =
[1,2,3,1,1,3]
1
2
3
[1,2,3,1,1,3]
[1,1,1,1]
[1,2,3]

Number of Steps to Reduce a Number in Binary Representation to One - LeetCode
