class Solution:
    def maxDiffSum(self, arr):
        # code here
        n = len(arr)
        
        dp = [[0] * 2 for _ in range(n)]
        
        for i in range(n - 1):
            dp[i + 1][0] = max(dp[i][0], dp[i][1] + abs(1 - arr[i]))
            
            dp[i + 1][1] = max(dp[i][0] + abs(arr[i + 1] - 1), dp[i][1] + abs(arr[i + 1] - arr[i]))
        return max(dp[n - 1][0], dp[n - 1][1])