
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []
        path = []

        def backtrack(start):

            result.append(path.copy())

            for i in range(start, len(nums)):

                # Skip duplicate elements
                if i > start and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])

                backtrack(i + 1)

                path.pop()

        backtrack(0)

        return result
