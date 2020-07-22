class Node: 
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None 

class Queue: 
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,valueInput):
        newNode = Node(valueInput)
        self.tail= newNode
        self.head = self.tail
        print(self.head)
        return self

    def dequeue(self):
        self.tail = None
        print(self.tail)
        return self


# def dequeu(self):

Q= Queue()
Q.enqueue(1).enqueue(2).dequeue()