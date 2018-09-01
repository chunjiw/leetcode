"""
158. Read N Characters Given Read4 II - Call multiple times
DescriptionHintsSubmissionsDiscussSolution
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times.

Example 1: 

Given buf = "abc"
read("abc", 1) // returns "a"
read("abc", 2); // returns "bc"
read("abc", 1); // returns ""
Example 2: 

Given buf = "abc"
read("abc", 4) // returns "abc"
read("abc", 1); // returns ""
"""

from collections import deque

class Solution(object):

    def __init__(self):
        self.cache = deque()
        self.buf4 = range(4)

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        index = 0  # number of chars read so far
        while n:
            if self.cache:
                buf[index] = self.cache.popleft()
                index += 1
                n -= 1
            else:
                l = read4(self.buf4)
                if not l:
                    return index                
                for i in range(l):
                    if n:
                        buf[index] = self.buf4[i]
                        index += 1
                        n -= 1
                    else:
                        self.cache.append(self.buf4[i])               
        return index

