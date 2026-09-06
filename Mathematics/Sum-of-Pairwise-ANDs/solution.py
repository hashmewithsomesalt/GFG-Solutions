class Solution:
    def pairAndSum(self, arr):
        # code here
        ans = 0
        n = len(arr)
        for i in range(32):
            k = 0
            for j in range(n):
                if (arr[j] & (1 << i)):
                    k += 1
            ans += (1 << i) * (k * (k - 1) // 2)
        return ans