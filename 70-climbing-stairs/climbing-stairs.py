class Solution(object):
    def climbStairs(self, n):
        

    # Create a dp array initialized with -1
        dp = [-1] * (n + 1)

    # Base cases
        dp[0] = 1
        dp[1] = 1

    # Fill dp array using bottom-up dynamic programming
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

    # Print the nth Fibonacci number
        return dp[n]
        