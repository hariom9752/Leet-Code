
import heapq

class Solution:
    def assignTasks(self, servers, tasks):

        available = []
        busy = []

        for i, weight in enumerate(servers):
            heapq.heappush(available, (weight, i))

        ans = []
        time = 0

        for i, task in enumerate(tasks):

            time = max(time, i)

            # Release all free servers
            while busy and busy[0][0] <= time:
                end, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))

            # Wait if no server is available
            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    end, weight, idx = heapq.heappop(busy)
                    heapq.heappush(available, (weight, idx))

            # Select best available server
            weight, idx = heapq.heappop(available)

            ans.append(idx)

            # Server becomes busy
            heapq.heappush(
                busy,
                (time + task, weight, idx)
            )

        return ans

