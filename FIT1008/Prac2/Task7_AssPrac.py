class stackADT:
    def __init__(self,size):
        assert size>0, "Size should be positive"
        self.theArray = size * [None]
        self.count = 0
        self.top = -1
    def size(self):
        return self.count

    def isEmpty(self):
        return self.size ==0

    def isFull(self):
        return self.size<=len(self.theArray)

    def reset(self):
        self.count = 0
        self.top=-1

    def push(self,newItem):
        if self.isFull():
            raise Exception ("Stack is full")
        self.top += 1
        self.theArray[self.top] = newItem
        self.count += 1

    def pop(self):
        if self.isEmpty():
            raise Exception ("Stack is empty")
        item = self.theArray[self.top]
        self.top -= 1
        self.count -= 1