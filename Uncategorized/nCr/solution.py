
class Solution:
    def nCr(self, n, r):
        if r < 0 or r > n:
            return 0

        r = min(r, n - r)
        result = 1

        for i in range(1, r + 1):
            result = result * (n - i + 1) // i

        return result