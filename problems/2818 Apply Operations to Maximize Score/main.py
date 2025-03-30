class Solution:

    def fast_exp(self, base, power, MOD):
        result = 1
        while power > 0:
            if power % 2 == 1:
                result = (result * base) % MOD
            base = (base * base) % MOD
            power //= 2
        return result

    def pscore(self, num, primes):
        if num in self.score:
            return self.score[num]
        numcopy = num
        p = 0
        result = 0
        while num > 1:
            if primes[p] * primes[p] > num:
                break
            if num % primes[p] == 0:
                result += 1
                while num % primes[p] == 0:
                    num //= primes[p]
            p += 1
        if num > 1:
            result += 1
        self.score[numcopy] = result
        return result

    def get_primes(self, limit):
        isprime = [True] * limit
        primes = []
        for i in range(2, limit):
            if not isprime[i]:
                continue
            primes.append(i)
            for j in range(i*i, limit, i):
                isprime[j] = False
        return primes

    def maximumScore(self, nums: List[int], k: int) -> int:
        # get all primes that are under max(nums)
        limit = max(nums) + 1
        primes = self.get_primes(limit)
        # get prime score for all num in nums
        self.score = {}
        scores = [self.pscore(num, primes) for num in nums]
        # monotonically decreasing stack to get left[] and right[]
        stack = []
        n = len(nums)
        left = [-1] * n 
        right = [n] * n
        for i, score in enumerate(scores):
            while stack and scores[stack[-1]] < score:
                j = stack.pop()
                right[j] = i
            # here stack is empty or scores[stack[-1]] >= score
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        # start operations: pick highest num first
        MOD = 1_000_000_007
        total_score = 1
        nums_index = [(num, i) for i, num in enumerate(nums)]
        nums_index.sort()
        while k > 0:
            x, i = nums_index.pop()
            # number of substrings that contains x
            power = min(k, (i - left[i]) * (right[i] - i))
            total_score *= self.fast_exp(x, power, MOD)
            total_score %= MOD
            k -= power
        return total_score