class Solution:
    def findSubtreeSizes(self, parent, s):
        n = len(parent)
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        path = [[] for _ in range(26)]

        def dfs(node):
            c = ord(s[node]) - ord('a')

            if path[c]:
                new_parent[node] = path[c][-1]

            path[c].append(node)

            for child in children[node]:
                dfs(child)

            path[c].pop()

        dfs(0)

        new_children = [[] for _ in range(n)]
        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        ans = [1] * n

        def calculate(node):
            for child in new_children[node]:
                calculate(child)
                ans[node] += ans[child]

        calculate(0)
        return ans