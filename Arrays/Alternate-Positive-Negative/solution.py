class Solution:
    def rearrange(self,arr):
        # code here
        pos_arr = []
        neg_arr = []
        
        for i in range(len(arr)):
            if arr[i] > -1:
                pos_arr.append(arr[i])
            else:
                neg_arr.append(arr[i])
        i = 0
        j = 0
        k = 0
        while (i < len(pos_arr) or j < len(neg_arr)):
            if (len(pos_arr) > i):
                arr[k] = pos_arr[i]
                i += 1
                k += 1
            if (len(neg_arr) > j):
                arr[k] = neg_arr[j]
                j += 1
                k += 1
                
        return arr