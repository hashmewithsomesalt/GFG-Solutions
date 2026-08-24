class Solution:
    def josephus(self, n, k):
        # code here
        k -= 1
        arr = [0] * n
        for i in range(n):
            arr[i] = 1
        
        cnt = 0
        cut = 0
        
        num = 1
        while (cnt < (n - 1)):
            while (num <= k):
                cut += 1
                cut = cut % n
                if (arr[cut] == 1):
                    num += 1
            num = 1
            arr[cut] = 0
            cnt += 1
            cut += 1
            
            cut = cut % n
            while (arr[cut] == 0):
                cut += 1
                cut = cut % n
        return cut + 1