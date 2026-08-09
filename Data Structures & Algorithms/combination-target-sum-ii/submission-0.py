class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        len_candidates = len(candidates)
        candidates.sort()
        def find_sum(i: int, total: int) -> None:
            if total == target:
                result.append(chosen.copy())
                return 

            start = i
            while i < len_candidates and total + candidates[i] <= target:
                while start < i < len_candidates and candidates[i - 1] == candidates[i]:
                    i += 1 
                if i == len_candidates:
                    return

                if total + candidates[i] > target:
                    return
                    
                chosen.append(candidates[i])
                find_sum(i + 1, total + candidates[i])
                chosen.pop()
                i += 1
            
            return 

        result = []
        chosen = []
        find_sum(0, 0)

        return result
        