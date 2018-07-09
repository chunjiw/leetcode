# 170. Two Sum III - Data structure design
# DescriptionHintsSubmissionsDiscussSolution
# Design and implement a TwoSum class. It should support the following operations: add and find.

# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.

# Example 1:

# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false
# Example 2:

# add(3); add(1); add(2);
# find(3) -> true
# find(6) -> false

class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bag = dict()
        self.nums = []
        self.len = 0

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.nums.append(number)
        if number not in self.bag:
            self.bag[number] = [self.len]
        else:
            self.bag[number].append(self.len)
        self.len += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for i in range(self.len):
            if value - self.nums[i] in self.bag:
                for j in self.bag[value - self.nums[i]]:
                    if j != i:
                        return True
                continue
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)