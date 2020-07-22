class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None


    def enqueue(self, valueInput):
        newnode = Node(valueInput)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = self.tail.next
        return self

    def dequeue(self):
        if self.head == None:
            print("nothing to remove")
            return self
        else:
            temp = self.head.value
            self.head = self.head.next
            return temp


    def display(self):
        runner = self.head
        print(runner)
        while runner != None:
            runner = runner.next
        return self

    def front(self): 
        if self.head == None: 
            print("nothing to return")
        else:
            return self.head

    def isempty(self): 
        if self.head == None: 
            return True
        else: 
            return False

    def size(self):
        q = Queue()
        print(len(q.qsize))








q1 = Queue()
q1.enqueue(5).enqueue(6).enqueue(7).size()
q1.front()