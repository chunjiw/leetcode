1404. Number of Steps to Reduce a Number in Binary Representation to One

Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:

    If the current number is even, you have to divide it by 2.

    If the current number is odd, you have to add 1 to it.

It is guaranteed that you can always reach one for all test cases.

 

Example 1:

Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.  
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1.  

Example 2:

Input: s = "10"
Output: 1
Explanation: "10" corresponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.  

Example 3:

Input: s = "1"
Output: 0

 

Constraints:

    1 <= s.length <= 500
    s consists of characters '0' or '1'
    s[0] == '1'

Hint 1
Read the string from right to left, if the string ends in '0' then the number is even otherwise it is odd.
Hint 2
Simulate the steps described in the binary string.
Similar Questions
Minimum Moves to Reach Target Score
Medium
Discussion (103)
💡 Discussion Rules

1. Please don't post any solutions in this discussion.

2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.

3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.
No comments yet.
Copyright ©️ 2025 LeetCode All rights reserved
4 Online
1
2
3
Saved
s =
"1101"
1
2
3
"1101"
"10"
"1"

Count Special Quadruplets - LeetCode
