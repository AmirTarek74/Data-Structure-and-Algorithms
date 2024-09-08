from LinkedList import *

class Stack:
    def __init__(self) -> None:
        self.stack = LinkedList()
        self.top = self.stack.tail
    
    def isEmpty(self) -> bool:
        return self.stack.size == 0

    def push(self, val) ->bool:
        if self.isEmpty():
            self.stack.insertFirst(val)
            self.top = self.stack.tail
        else:
            self.stack.insert(val)
            self.top = self.stack.tail
        return True
    
    def getTop(self) ->int:
        if self.isEmpty():
            return 0
        else:
            return self.top.val
    
    def pop(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.stack.delete(self.top.val)
            self.top = self.stack.tail
        return True
    
    def traverse(self):
        self.stack.traverse()
