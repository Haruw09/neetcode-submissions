class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        cur = []
        def dfs(start: int) -> None:
            result.append(cur.copy())
            for i in range(start, len(nums)):
                cur.append(nums[i])
                dfs(i + 1)
                cur.pop()
            return

        dfs(0)
        return result