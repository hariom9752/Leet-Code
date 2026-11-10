
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for jump in (1, 2, 3):
                if i - jump >= 0:
                    dp[i] = min(
                        dp[i],
                        dp[i-jump] + costs[i-1] + jump**2
                    )

        return dp[n]
