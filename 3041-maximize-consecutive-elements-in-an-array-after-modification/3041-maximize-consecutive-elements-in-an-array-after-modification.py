class Solution(object):
    def maxSelectedElements(self, nums):
        nums.sort()
        dp = {}

        for x in nums:
            a = dp.get(x, 0)
            b = dp.get(x - 1, 0)

            dp[x + 1] = max(dp.get(x + 1, 0), a + 1)
            dp[x] = max(dp.get(x, 0), b + 1)

        return max(dp.values())