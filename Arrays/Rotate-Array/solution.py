class Solution:
    def rotateArr(self, arr, d):
        # code here
        d %= len(arr)
        arr[:] = arr[d:] + arr[:d]
        return arr