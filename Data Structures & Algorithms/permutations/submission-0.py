class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        cur = []
        len_nums = len(nums)
        fixed = set()
        def find_perm(step: int) -> None:
            if step == len_nums:
                result.append(cur.copy())
                return

            for i in range(len_nums):
                if nums[i] in fixed:
                    continue

                cur.append(nums[i])
                fixed.add(nums[i])

                find_perm(step + 1)

                cur.pop()
                fixed.remove(nums[i])

        find_perm(0)
        return result