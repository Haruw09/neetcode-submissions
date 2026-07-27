class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_end = 0
        farthest = 0
        jumps_num = 0
        i = 0
        while i < len(nums):
            while i <= cur_end < len(nums):
                farthest = max(i + nums[i], farthest)
                i += 1
            if cur_end < len(nums) - 1 and farthest > 0:
                jumps_num += 1
                cur_end = farthest
                farthest = 0
            else:
                return jumps_num
                
            
            
        
            
