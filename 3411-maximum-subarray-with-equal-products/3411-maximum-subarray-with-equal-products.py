from math import gcd

class Solution:
    def maxLength(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 1

        for i in range(n):
            prod = 1
            g = 0
            l = 1

            for j in range(i, n):
                x = nums[j]

                prod *= x
                g = gcd(g, x)
                l = (l * x) // gcd(l, x)

                if prod == g * l:
                    ans = max(ans, j - i + 1)

        return ans