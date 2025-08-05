class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        def sidesteps(n, left, right):
            ans = 0
            while left <= n:
                ans += min(n+1, right) - left
                left *= 10
                right *= 10
            return ans

        current = 1
        k -= 1
        while k > 0:
            steps = sidesteps(n, current, current+1)
            if k - steps >= 0:
                k -= steps
                current += 1
            else:
                current *= 10
                k -= 1
                

        return current






        # D = 0
        # nn = n
        # while nn > 0:
        #     D += 1
        #     nn //= 10

        # nn = n
        # ndigits = []
        # while nn:
        #     ndigits.append(nn % 10)
        #     nn //= 10
        
        # def unit(level):
        #     res = 1
        #     for _ in range(level):
        #         res *= 10
        #         res += 1
        #     return res

        # def value(digits):
        #     return int(''.join([str(d) for d in digits]))
        
        # rank = 0
        # digits = []
        # level = D - 1

        # while rank <= k and level >= 0:
        #     rank += 1
        #     digit = 0 if rank > 1 else 1    # count up from 0 (1 if at the very start)
        #     while rank + unit(level) <= k and digit < ndigits[level]:
        #         rank += unit(level)
        #         digit += 1
        #     digits.append(digit)
        #     if rank == k:
        #         return digits
        #     level -= 1

        # level = 0
        # digits.pop()
        # while rank <= k and level < D-1:
        #     while rank + unit(level) <= k and digits[-1] < 9:
        #         rank += unit(level)
        #         digits[-1] += 1
        #     if rank == k:
        #         return digits  # ??
        #     level += 1
        #     rank += 1
        #     digits.pop()
        
        # return digits

        # while rank <= k and level >= 0:
        #     while rank + unit(level) <= k and digit < ndigits[level]:
        #         rank += unit(level)
        #         digit += 1
        #     digits.append(digit)
        #     if rank == k:
        #         return digits
        #     digit = 0
        #     rank += 1
        #     level -= 1

        # return digits




        


sol = Solution()
# print(sol.findKthNumber(9999, 1111))
# print(sol.findKthNumber(9999, 1112))
# print(sol.findKthNumber(9999, 1113))

print(sol.findKthNumber(4356, 3731))
print(sol.findKthNumber(4356, 3732))
print(sol.findKthNumber(4356, 3733))
print(sol.findKthNumber(4356, 3734))
print(sol.findKthNumber(4356, 3735))
print(sol.findKthNumber(4356, 3736))

# print(sol.findKthNumber(4350, 3724))
# print(sol.findKthNumber(4350, 3725))


# print(sol.findKthNumber(1, 1))
# print(sol.findKthNumber(2, 1))
# print(sol.findKthNumber(2, 2))


# print(sol.findKthNumber(11, 5))





# print(sol.findKthNumber(4356, 3732))


        