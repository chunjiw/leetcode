class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        stack = []    # id, starttime, timeloss
        result = [0] * n
        for log in logs:
            id, event, timestamp = log.split(':')
            id = int(id)
            timestamp = int(timestamp)
            if not stack or event == 'start':
                stack.append([id, timestamp, 0])
            else:
                _, starttime, losstime = stack.pop()
                result[id] += timestamp - starttime + 1 - losstime
                if stack:
                    stack[-1][2] += timestamp - starttime + 1
        return result
    
sol = Solution()
print(sol.exclusiveTime(2, ['0:start:0', '1:start:2', '1:end:5', '0:end:6']))
print(sol.exclusiveTime(1, ['0:start:0', '0:start:2', '0:end:5', '0:start:6', '0:end:6', '0:end:7']))
