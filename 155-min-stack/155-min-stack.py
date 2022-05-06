class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min: self.min = val    

    def pop(self) -> None:
        popped = self.stack.pop()
        
        if not self.min in self.stack:
            newMin = float('inf')
            
            for val in self.stack:
                if val < newMin:
                    newMin = val
            self.min = newMin

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()