class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path, remaining):
            if not remaining:
                result.append(path[:])
                return

            for i in range(len(remaining)):
                path.append(remaining[i])

                backtrack(path, remaining[:i] + remaining[i+1:])

                path.pop()

        backtrack([], nums)
        return result