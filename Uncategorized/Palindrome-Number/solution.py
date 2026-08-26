class Solution:
    def isPalindrome(self, n):
		# code here
		reverse = 0
		temp = abs(n)
		
		while (temp > 0):
		    reverse = (reverse * 10) + temp % 10
		    temp //= 10
	    return reverse == abs(n)