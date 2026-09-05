class Solution:
    def longestSubseq(self, arr):
        # code here
        n = len(arr)
        
        if n == 1:
            return 1
            
        dp = {}
        ans = 1
        
        for i in range(n):
            if arr[i] + 1 in dp or arr[i] - 1 in dp:
                dp[arr[i]] = 1 + max(dp.get(arr[i] + 1, 0), dp.get(arr[i] - 1, 0))
            else:
                dp[arr[i]] = 1
                
            
            ans = max(ans, dp[arr[i]])
            
        return ans