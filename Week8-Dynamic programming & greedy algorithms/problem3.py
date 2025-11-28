class Solution:
    def maxSubArray(self, nums):
        current_sum = max_sum = nums[0]
        
        for n in nums[1:]:
            # either extend the previous subarray or start fresh
            current_sum = max(n, current_sum + n)
            max_sum = max(max_sum, current_sum)
        
        return max_sum
