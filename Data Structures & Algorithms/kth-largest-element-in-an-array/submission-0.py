class Solution:
    def partition(self, nums: list[int], left: int, right: int):
        if nums[left] < nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left + 1] < nums[right]:
            nums[left + 1], nums[right] = nums[right], nums[left + 1]
        if nums[left] < nums[left + 1]:
            nums[left], nums[left + 1] = nums[left + 1], nums[left]

        pivot = nums[left + 1]
        i = left + 1
        j = right
        while i < j:
            i += 1
            while nums[i] > pivot:
                i += 1
            
            j -= 1
            while nums[j] < pivot:
                j -= 1

            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]

        nums[left + 1], nums[j] = nums[j], nums[left + 1]
        return j

    def findKthLargest(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            if left + 1 == right:
                if nums[left] < nums[right]:
                    nums[left], nums[right] = nums[right], nums[left]
                break
            cur_partition = self.partition(nums, left, right)
            if cur_partition == k - 1:
                break
            elif cur_partition > k - 1:
                right = cur_partition - 1
            else:
                left = cur_partition + 1

        return nums[k - 1]