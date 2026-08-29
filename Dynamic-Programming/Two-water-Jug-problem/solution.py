class Solution:
	def minSteps(self, m, n, d):
		# Code here
		if d == 0:
		    return 0
		    
		if d > max(m, n):
		    return -1
		    
		if d % self.gcd(m, n) != 0:
		    return -1
		    
		return min(self.pour(m, n, d), self.pour(n, m, d))
		
	def gcd(self, m, n):
	    if m == 0:
	        return n
	    
	    return self.gcd(n % m, m)
	    
	def pour(self, m, n, d):
	    fromJug = m
	    toJug = 0
	    
	    steps = 1
	    
	    while (fromJug != d) and (toJug != d):
	        temp = min(fromJug, n - toJug)
	        fromJug -= temp
	        toJug += temp
	        steps += 1
	        
	        if (fromJug == d) or (toJug == d):
	            break
	        
	        if (fromJug == 0):
	            fromJug = m
	            steps += 1
	            
	        if toJug == n:
	            toJug = 0
	            steps += 1
	            
	    return steps