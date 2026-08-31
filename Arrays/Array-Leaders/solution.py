class Solution:
    def leaders(self, arr):
        # code here
        ans = []
        highest = float('-inf')
        
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] >= highest:
                ans.append(arr[i])
                highest = arr[i]
                
        return ans[::-1]