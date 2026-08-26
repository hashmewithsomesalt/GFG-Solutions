class Solution:
    def isPalindrome(self, n):
		# code here
		mystr = str(abs(n))
		
		for i in range((len(mystr)// 2) + 1):
		    if mystr[i] != mystr[len(mystr) - i - 1]:
		        return False
		return True
		    