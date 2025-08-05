class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        return self.numPower(finish, limit, s) - self.numPower(start-1, limit, s)
    
    def numPower(self, finish, limit, s):
        if finish < int(s):
            return 0
        if len(str(finish)) == len(s):
            return 1
        nf = len(str(finish))
        ns = len(s)
        # number of free digits
        nd = nf - ns
        # first digit of finish
        ff = int(str(finish)[0])
        if ff > limit:
            return (limit+1) ** nd
        else:
            # here guaranteed str(finish)[1:] is not empty because finish >= s and they cannot both be length 1
            return ff * (limit+1) ** (nd-1) + self.numPower(int(str(finish)[1:]), limit, s)

        # total_count = 0
        # curr = 1
        # for i in range(int(str(finish[0]))):
        #     if i <= limit
        # for i in range(nd):
        #     curr += limit
        #     total_count += limit * curr
        # count = int(finish[:nd]) + 1
        # return count

sol = Solution()
print(sol.numberOfPowerfulInt(1, 6000, 4, '124'))
print(sol.numberOfPowerfulInt(1, 40000, 4, '124'))
print(sol.numberOfPowerfulInt(15, 215, 6, '10'))
print(sol.numberOfPowerfulInt(1000, 2000, 4, '3000'))