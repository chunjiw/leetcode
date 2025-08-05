class Solution:

    def calculate(self, nums, ops):
        if not ops:
            return nums
        result = []
        for i in range(len(ops)):
            left = self.calculate(nums[0:i+1], ops[0:i])
            right = self.calculate(nums[i+1:], ops[i+1:])
            for n1 in left:
                for n2 in right:
                    if ops[i] == '+':
                        result.append(n1 + n2)
                    elif ops[i] == '-':
                        result.append(n1 - n2)
                    else:
                        result.append(n1 * n2)
        return result

    def diffWaysToCompute(self, expression: str) -> List[int]:
        nums = []
        ops = []
        num = 0
        for s in expression:
            if s.isdigit():
                num *= 10
                num += int(s)
            else:
                nums.append(num)
                num = 0
                ops.append(s)
        nums.append(num)
        return self.calculate(nums, ops)

        