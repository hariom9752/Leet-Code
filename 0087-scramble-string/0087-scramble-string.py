
from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        if s1 == s2:
            return True

        if sorted(s1) != sorted(s2):
            return False

        n = len(s1)

        @lru_cache(None)
        def solve(a, b, length):

            if s1[a:a+length] == s2[b:b+length]:
                return True

            if sorted(s1[a:a+length]) != sorted(s2[b:b+length]):
                return False

            for k in range(1, length):

                # Without swapping
                if (solve(a, b, k) and
                    solve(a+k, b+k, length-k)):
                    return True

                # With swapping
                if (solve(a, b+length-k, k) and
                    solve(a+k, b, length-k)):
                    return True

            return False

        return solve(0, 0, n)
