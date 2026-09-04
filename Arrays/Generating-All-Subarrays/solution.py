class Solution:
    def getSubArrays(self, arr):
        #code here
        #creation of a answer list
        ans = []
        
        for i in range(len(arr)):
            myarr = []
            for j in range(i, len(arr)):
                myarr.append(arr[j])
                ans.append(myarr.copy())
        return ans