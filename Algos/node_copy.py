class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None

class sll:
    def __init__(self):
        self.head = None
    def addfront(self, valueInput):
        #createNewNode
        newnode = Node(valueInput)
        newnode.next = self.head
        self.head = newnode
        return self

    def removefront(self):
        if self.head == None:
            print ('This list empty, YEET')
            return self
        newfront = self.head.next
        self.head = newfront
        return self

    def display(self):
        runner = self.head
        while runner.next is not None:
            runner = runner.next
            print(runner)
        return self

    def addback(self,valueInput):
        newnode = Node(valueInput)
        runner = self.head
        while runner != None:
            runner = runner.next
        runner.next = newnode
        return self

    def removeBack(self): 
        runner = self.head
        while(runner.next is not None):
            prev = runner
            runner = runner.next
        prev.next = None




            


sll1 = sll()
sll1.addfront(10).addfront(9).removeBack().display()

