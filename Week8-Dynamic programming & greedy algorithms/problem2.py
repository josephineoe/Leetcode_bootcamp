class Solution:
    def coinChange(self, coins, amount):
        # Large placeholder (amount+1 is effectively infinity)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        
        return dp[amount] if dp[amount] != amount + 1 else -1
