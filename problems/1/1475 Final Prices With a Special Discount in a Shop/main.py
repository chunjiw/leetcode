class Solution:

    def finalPrices(self, prices: List[int]) -> List[int]:
        for i, price in enumerate(prices):
            for p in prices[i+1:]:
                if p <= price:
                    prices[i] -= p
                    break
        return prices

    def finalPrices_one_pass(self, prices: List[int]) -> List[int]:
        stack = []
        result = list(prices)
        for i, price in enumerate(prices):
            if not stack or price > prices[stack[-1]]:
                stack.append(i)
                continue
            while stack and price <= prices[stack[-1]]:
                j = stack.pop()
                result[j] = prices[j] - price
            stack.append(i)
        return result
