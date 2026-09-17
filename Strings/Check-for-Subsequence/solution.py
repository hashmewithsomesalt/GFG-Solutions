class Solution:
    def isSubSeq(self, s1, s2):
        # code here
        count = 0
        for i in range(len(s2)):
            if count == len(s1):
                return True
            if s2[i] == s1[count]:
                count += 1
        return count == len(s1)