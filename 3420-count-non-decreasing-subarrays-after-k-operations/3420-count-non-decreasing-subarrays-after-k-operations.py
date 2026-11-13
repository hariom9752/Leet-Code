
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        nxt = [n] * n
        st = []

        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] <= nums[i]:
                st.pop()

            if st:
                nxt[i] = st[-1]

            st.append(i)

        LOG = n.bit_length()

        up = [[n] * (n + 1) for _ in range(LOG)]
        cost = [[0] * (n + 1) for _ in range(LOG)]

        for i in range(n):
            j = nxt[i]
            up[0][i] = j
            cost[0][i] = nums[i] * (j - i) - (pref[j] - pref[i])

        for p in range(1, LOG):
            for i in range(n):
                mid = up[p - 1][i]
                up[p][i] = up[p - 1][mid]
                cost[p][i] = cost[p - 1][i] + cost[p - 1][mid]

        def get_cost(l, r):
            cur = l
            total = 0

            for p in range(LOG - 1, -1, -1):
                j = up[p][cur]

                if j <= r:
                    total += cost[p][cur]
                    cur = j

            if cur < r:
                total += nums[cur] * (r - cur)
                total -= pref[r + 1] - pref[cur + 1]

            return total

        ans = 0
        r = 0

        for l in range(n):
            if r < l:
                r = l

            while r < n and get_cost(l, r) <= k:
                r += 1

            ans += r - l

        return ans
