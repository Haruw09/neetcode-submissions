class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        len_candidates = len(candidates)
        candidates.sort()
        def find_sum(start: int, total: int) -> None:
            if total == target:
                result.append(chosen.copy())
                return 

            for i in range(start, len_candidates):
                if i > start and candidates[i - 1] == candidates[i]:
                    continue

                if total + candidates[i] > target:
                    break

                chosen.append(candidates[i])
                find_sum(i + 1, total + candidates[i])
                chosen.pop()
                i += 1
            
            return 

        result = []
        chosen = []
        find_sum(0, 0)

        return result
        