class Solution:
    def pivotIndex(self, nums: [int]) -> int:

        total = sum(nums)
        left_sum = 0

        for idx, val in enumerate(nums):
            right_sum = total - left_sum - val
            if left_sum == right_sum:
                return idx
            left_sum += val
            
        return -1
    
