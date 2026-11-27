class Solution:
    def maximumSaleItems(self, items, budget):
        n = len(items)

        bonus = [0] * n

        for i in range(n):
            factor_i = items[i][0]

            for j in range(n):
                if i != j and items[j][0] % factor_i == 0:
                    bonus[i] += 1

        min_price = min(price for factor, price in items)

        dp = [0] * (budget + 1)

        for i in range(n):
            factor, price = items[i]
            value = 1 + bonus[i]

            for b in range(budget, price - 1, -1):
                dp[b] = max(dp[b], dp[b - price] + value)

        ans = 0

        for spent in range(budget + 1):
            extra = (budget - spent) // min_price
            ans = max(ans, dp[spent] + extra)

        return ans