class Solution:
    def josephus(self, n, k):
        # code here
        i = 1
        ans = 0
        
        while (i <= n):
            ans = (ans + k) % i
            i += 1
            
        return ans + 1