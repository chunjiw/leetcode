# 3. Longest Substring Without Repeating Characters
# DescriptionHintsSubmissionsDiscussSolution
# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        i, j = 0, 0 # [i,j) is the substring
        result = 0
        letter = set()
        while j < len(s):
            if s[j] not in letter:
                letter.add(s[j])
                result = max(result, len(letter))
                j += 1
            else:
                while s[i] != s[j]:
                    letter.remove(s[i])
                    i += 1
                letter.remove(s[i])
                i += 1
        return result
                        
                
            
