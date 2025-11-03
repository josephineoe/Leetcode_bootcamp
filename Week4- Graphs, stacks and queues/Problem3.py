MOD = 10**9 + 7

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1  # day 1: one person learns the secret
        sharing = 0  # people eligible to share today

        for i in range(2, n + 1):
            # people who start sharing today
            if i - delay >= 1:
                sharing = (sharing + dp[i - delay]) % MOD
            # people who forget today (can't share today)
            if i - forget >= 1:
                sharing = (sharing - dp[i - forget]) % MOD
            # new learners today
            dp[i] = sharing

        # sum of those who still remember at day n
        start = max(1, n - forget + 1)
        return sum(dp[start : n + 1]) % MOD