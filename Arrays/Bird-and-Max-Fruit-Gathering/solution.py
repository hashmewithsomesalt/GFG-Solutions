class Solution:

    def maxFruits(self, arr: list[int], m: int) -> int:
        """ code here """
        if m == 0:
            return 0
        if m == 1:
            return max(arr)
            
        n = len(arr)
        
        current = sum(arr[0:m])
        maximum = current
        
        for i in range(n):
            current = current + arr[(i + m) % n] - arr[i % n]
            maximum = max(maximum, current)
        return maximum