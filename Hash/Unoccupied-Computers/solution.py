class Solution:
    def solve(self, n, s):
        # code here
        occupied = set()
        rejected = set()
        count = 0
        
        for ch in s:
            if ch not in occupied and ch not in rejected:
                if n <= len(occupied):
                    count += 1
                    rejected.add(ch)
                else:
                    occupied.add(ch)
            elif ch in occupied:
                occupied.discard(ch)
                
        return count