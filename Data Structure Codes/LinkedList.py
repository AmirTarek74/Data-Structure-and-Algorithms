class Node:
    def __init__(self, val=0, next=None) -> None:
        
        self.val = val
        self.next = next 


class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
    
    def isEmpty(self) -> bool:
        return self.size == 0

    def insert(self, val) -> bool:
        if self.isEmpty():
            return self.insertFirst(val)
        else:
            node = Node(val)
            self.tail.next = node 
            self.tail = node 
            self.size += 1
            return True
    
    def insertFirst(self,val) -> bool:
        if self.size == 0:
            self.head = Node(val)
            self.tail = self.head
            self.size +=1
            
        else:
            node = Node(val)
            node.next = self.head 
            self.head = node 
            self.size +=1
            
        return True
    
    def insertPosition(self, val, pos) -> bool:
        if pos == 1:
            return self.insertFirst(val)
        elif pos == self.size + 1:
            return self.insert(val) 
        elif 1<pos<=self.size:
            c = 1
            prev = None
            curr = self.head
            while c<pos:
                c+=1
                prev = curr
                curr = curr.next
            node = Node(val)
            prev.next = node
            node.next = curr 
            self.size +=1
            return True
        return False
    
    def traverse(self) -> None:
        res = []
        ptr = self.head
        while ptr:
            res.append(ptr.val) 
            ptr = ptr.next
        
        print(f"Current Nodes {res}")

    def delete(self, val)-> bool:
        if self.isEmpty():
            return False
        elif self.head.val == val:
            return self.deleteFirst()
        else:
            ptr = self.head
            prev = None
            while ptr!= None and ptr.val != val  :
                prev = ptr
                ptr = ptr.next
            if ptr == None:
                return False
            if ptr== self.tail:
                self.tail = prev
            prev.next = ptr.next
            ptr.next = None
            self.size -=1
            return True

    
    def deleteFirst(self) -> bool:
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.size = 0
            return True
        else:
            ptr = self.head
            self.head = self.head. next
            ptr.next = None
            self.size -= 1
            return True
            




            