class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []
        bag = set()
        for let in s:
            if let not in bag:
                while stack and stack[-1] > let and count[stack[-1]] > 0:
                    bag.remove(stack.pop())
                stack.append(let)
                bag.add(let)
            count[let] -= 1
        return ''.join(stack)

