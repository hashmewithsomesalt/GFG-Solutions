class Solution:
    def minCount(self, arr):
        """ code here """
        n = len(arr)
        
        next = [[0] * (n + 1) for _ in range(n + 1)]
        curr = [[0] * (n + 1) for _ in range(n + 1)]
        
        for idx in range(n - 1, -1, -1):
            for incLast in range(-1, n):
                for decLast in range(-1, n):
                    ans = 1 + next[incLast + 1][decLast + 1]
                    
                    if incLast == -1 or arr[idx] > arr[incLast]:
                        ans = min(ans, next[idx + 1][decLast + 1])
                        
                    if decLast == -1 or arr[idx] < arr[decLast]:
                        ans = min(ans, next[incLast + 1][idx + 1])
                    
                    curr[incLast + 1][decLast + 1] = ans
            next, curr = curr, next
        
        return next[0][0]