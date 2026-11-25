class Solution:
    def smallestUniqueSubarray(self, nums):
        n = len(nums)

        # Build Suffix Array
        sa = list(range(n))
        rank = nums[:]
        k = 1

        while k < n:
            sa.sort(key=lambda i: (
                rank[i],
                rank[i + k] if i + k < n else -1
            ))

            new_rank = [0] * n

            for j in range(1, n):
                prev = sa[j - 1]
                curr = sa[j]

                prev_key = (
                    rank[prev],
                    rank[prev + k] if prev + k < n else -1
                )

                curr_key = (
                    rank[curr],
                    rank[curr + k] if curr + k < n else -1
                )

                new_rank[curr] = new_rank[prev] + (prev_key != curr_key)

            rank = new_rank

            if rank[sa[-1]] == n - 1:
                break

            k *= 2

        # Build inverse suffix array
        pos = [0] * n

        for i in range(n):
            pos[sa[i]] = i

        # Build LCP array using Kasai algorithm
        lcp = [0] * n
        h = 0

        for i in range(n):
            r = pos[i]

            if r == 0:
                continue

            j = sa[r - 1]

            while (
                i + h < n
                and j + h < n
                and nums[i + h] == nums[j + h]
            ):
                h += 1

            lcp[r] = h

            if h > 0:
                h -= 1

        # Find minimum unique subarray length
        ans = n

        for r in range(n):
            i = sa[r]

            left_lcp = lcp[r]
            right_lcp = lcp[r + 1] if r + 1 < n else 0

            max_lcp = max(left_lcp, right_lcp)

            length = max_lcp + 1

            if length <= n - i:
                ans = min(ans, length)

        return ans