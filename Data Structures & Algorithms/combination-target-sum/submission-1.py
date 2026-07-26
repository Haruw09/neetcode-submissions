class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        cur = []
        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(cur.copy())
                return

            for i in range(start, len(nums)):
                number = nums[i]
                if number > remaining:
                    continue

                cur.append(number)
                backtrack(i, remaining - number)
                cur.pop()

        backtrack(0, target)
        return result