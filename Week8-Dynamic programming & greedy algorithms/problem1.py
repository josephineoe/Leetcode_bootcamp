class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        
        # If total sum is odd, cannot partition evenly
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        # dp[s] = whether a subset sum s is possible
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            # iterate backwards to avoid reuse
            for s in range(target, num - 1, -1):
                dp[s] |= dp[s - num]
        
        return dp[target]
