class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None

class Queue: 
    def __init__(self):
        self.head = None
        self.tail = None

class Stack: 
    def __init__(self):
        self.top = None 

    def push(self, valueInput):
        newnode = Node(valueInput)
        if self.top == None:
            self.top = newnode
        else: 
            newnode.next = self.top
            self.top = newnode
        return self

    def display(self):
        runner = self.top
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self
    
    def topreturn(self):
        runner = self.top
        if runner != None: 
            print(runner.value)
        if runner == None: 
            print("nothing on top")
        return self

    def isempty(self):
        runner = self.top
        if runner == None:
            return True
        if runner != None: 
            return False
        return self

    def contains(self, valueInput):
        newnode = Node(valueInput)
        runner = self.top
        if runner == newnode: 
            print("FOUND")
        else:
            print("not found")
        return self
        



    

newstk = Stack()
newstk.push(5).push(15).display().topreturn().contains(4)

