class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        cur = []
        nums_len = len(nums)
        nums.sort()
        def find_subsets(start: int) -> None:
            result.append(cur.copy())

            for i in range(start, nums_len):
                if start < i and nums[i - 1] == nums[i]:
                    continue

                cur.append(nums[i])
                find_subsets(i + 1)
                cur.pop()

            return

        find_subsets(0)
        return result