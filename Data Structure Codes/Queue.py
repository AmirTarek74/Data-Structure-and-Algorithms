from LinkedList import *

class Queue:

    def __init__(self) ->None:
        self.queue = LinkedList()
        self.front = self.queue.head
        self.rear = self.queue.tail
        self.size = 0
    
    def isEmpty(self):
        return  self.size==0
    
    def enqueue(self,val) -> bool:
        if self.isEmpty():
            self.queue.insertFirst(val)
            self.front = self.queue.head
            self.rear = self.queue.tail
            self.size += 1
        else:
            self.queue.insert(val)
            self.front = self.queue.head
            self.rear = self.queue.tail
            self.size += 1
        return True
    
    def dequeue(self) -> int:
        if self.isEmpty():
            return -1

        else:
            value = self.queue.head.val
            self.queue.deleteFirst()
            self.front = self.queue.head
            self.rear = self.queue.tail
            self.size -= 1
            return value
    
    def traverse(self) ->None:
        if self.isEmpty():
            print("Queue is currently empty")
        else:
            self.queue.traverse()



