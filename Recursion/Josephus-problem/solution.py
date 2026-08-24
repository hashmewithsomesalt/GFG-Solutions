class Solution:
    def josephus(self, n, k):
        # code here
        def helpfunc(person, k, index):
            if len(person) == 1:
                return person[0]
            
            index = (index + k - 1) % len(person)
            person.pop(index)
            
            return helpfunc(person, k, index)

        person = []
        
        for i in range(1, n + 1):
            person.append(i)
        return helpfunc(person, k, 0)
        