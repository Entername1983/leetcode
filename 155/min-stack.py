class MinStack:
    def __init__(self):
        self.stack: list = []
        self.min_stack: list = [] # holds the min value
    
    
    def push(self, val: int) -> None:
        ## place as the last element of the array
        n: int = len(self.stack)
        self.stack.append(val)
        ## look at previous min value, set it at that
        ## if there is no previous min value (array is 0), then set it to val
        if not self.min_stack:
            ## if the stack is empty then val must be the lowest
            self.min_stack.append(val)
        else:
            ## else compare the previous minimum.  If its higher append the new value, which must be lower
            if self.min_stack[n - 1] > val:
                self.min_stack.append(val)
            else:
                self.min_stack.append(self.min_stack[n - 1])
        print(self.stack)
        print(self.min_stack)
        
    def pop(self) -> None:
        ## will this throw an index error if at 0?
        self.stack = self.stack[:-1]
        self.min_stack = self.min_stack[:-1]
        
    def top(self) -> int:
        n: int = len(self.stack)
        return self.stack[n - 1]
        
    def getMin(self) -> int:
        n: int = len(self.stack)
        return self.min_stack[n - 1]