class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        len_1 = len(nums1)
        len_2 = len(nums2)

        left_half_border = (len_1 + len_2 + 1) // 2

        left = 0
        right = len_1
        while left <= right:
            mid_1 = (left + right) // 2
            mid_2 = left_half_border - mid_1

            left_1 = nums1[mid_1 - 1] if mid_1 - 1 >= 0 else -float('inf')
            right_1 = nums1[mid_1] if mid_1 < len_1 else float('inf')
            left_2 = nums2[mid_2 - 1] if mid_2 - 1 >= 0 else -float('inf')
            right_2 = nums2[mid_2] if mid_2 < len_2 else float('inf')

            if left_1 <= right_2 and left_2 <= right_1:
                if (len_1 + len_2) % 2 == 1:
                    return float(max(left_1, left_2))
                else:
                    return (max(left_1, left_2) + min(right_1, right_2)) / 2
            elif left_1 > right_2:
                right = mid_1 - 1
            else:
                left = mid_1 + 1

        
