
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:

        n = len(arrival)

        # Segment Tree
        size = 1
        while size < k:
            size *= 2

        tree = [0] * (2 * size)

        for i in range(k):
            tree[size + i] = 1

        for i in range(size - 1, 0, -1):
            tree[i] = tree[2 * i] + tree[2 * i + 1]

        # Update server availability
        def update(pos, val):
            idx = size + pos
            tree[idx] = val

            idx //= 2
            while idx:
                tree[idx] = tree[2 * idx] + tree[2 * idx + 1]
                idx //= 2

        # Find first available server in range
        def find_first(ql, qr):

            def search(node, left, right):
                if right < ql or left > qr or tree[node] == 0:
                    return -1

                if left == right:
                    return left

                mid = (left + right) // 2

                ans = search(node * 2, left, mid)

                if ans != -1:
                    return ans

                return search(node * 2 + 1, mid + 1, right)

            return search(1, 0, size - 1)

        busy = []
        count = [0] * k

        for i in range(n):

            # Release completed servers
            while busy and busy[0][0] <= arrival[i]:
                end, server = heapq.heappop(busy)
                update(server, 1)

            start = i % k

            # Find next available server
            server = find_first(start, k - 1)

            if server == -1:
                server = find_first(0, start - 1)

            if server == -1:
                continue

            # Assign request
            update(server, 0)
            count[server] += 1

            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )

        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]
