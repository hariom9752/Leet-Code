
class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):

            # Single digit decoding
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # Two digit decoding
            if i >= 2:
                two = int(s[i - 2:i])

                if 10 <= two <= 26:
                    dp[i] += dp[i - 2]

        return dp[n]
