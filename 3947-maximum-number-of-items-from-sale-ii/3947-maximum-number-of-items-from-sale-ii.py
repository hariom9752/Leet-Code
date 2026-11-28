class Solution:
    def maximumSaleItems(self, items, budget):
        n = len(items)

        # Count frequency of each factor
        freq = [0] * (n + 1)

        minPrice = float('inf')

        for factor, price in items:
            freq[factor] += 1
            minPrice = min(minPrice, price)

        # Calculate how many item types each factor can unlock
        gain = [0] * (n + 1)

        for f in range(1, n + 1):
            total = 0

            for multiple in range(f, n + 1, f):
                total += freq[multiple]

            gain[f] = total - 1

        # Beneficial deals: cost less than buying 2 cheapest items
        deals = []

        for factor, price in items:
            if gain[factor] > 0 and price < 2 * minPrice:
                deals.append((price, gain[factor]))

        # Buy cheaper deals first
        deals.sort()

        ans = 0

        # Purchase deal copies
        for price, count in deals:
            if budget < price:
                break

            buy = min(count, budget // price)

            budget -= buy * price
            ans += buy * 2

        # Spend remaining budget on cheapest regular items
        ans += budget // minPrice

        return ans