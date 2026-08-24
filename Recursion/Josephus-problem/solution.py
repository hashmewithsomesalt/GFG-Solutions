class Solution:
    def josephus(self, n, k):
        # code here
        def helpingfunc(person, k, index):
            if len(person) == 1:
                return person[0]
                
            index = (index + k - 1) % len(person)
            person.pop(index)
            
            return helpingfunc(person, k, index)
        
        person = []
        
        for i in range(1, n + 1):
            person.append(i)
        
        return helpingfunc(person, k, 0)