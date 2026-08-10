class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        changed = 0
        max_seq = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                changed += 1
                while changed > k:
                    if nums[left] == 0:
                        changed -= 1
                    left += 1

            max_seq = max(right - left + 1, max_seq)

        return max_seq    

                
                