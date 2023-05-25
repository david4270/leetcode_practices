# 155. Min Stack - Medium - https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.values = []
        self.minVal = []       

    def push(self, val: int) -> None:
        
        
        if not self.values:
            self.values.append(val)
            self.minVal.append(val)
        else:
            self.values.append(val)
            self.minVal.append(min(self.minVal[-1],val))

    def pop(self) -> None: 
        del self.minVal[-1]  
        del self.values[-1]
         

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.minVal[-1]