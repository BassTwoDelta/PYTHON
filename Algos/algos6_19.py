class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None


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
    #another implementation of push
    def push2(self, valueInput):
        newnode = Node(valueInput)
        temp = self.top
        self.top = newnode
        self.top.next = temp
        return self

    def display(self):
        runner = self.top
        # print(runner)
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self

    def returntop(self):
        if self.top == None:
            print('nothing to return fam. no top')
            return self
        else:
            print(self.top.value)
            return self.top.value

    def isempty(self):
        if self.top == None:
            return True
        else:
            return False

    def pop(self):
        if self.top != None:
            tempvalue = self.top.value
            self.top = self.top.next
            return tempvalue, self
        else:
            print("no top to pop")
            return self

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
            print("nothing to remove fam")
            return self
        else:
            temp = self.head.value
            self.head = self.head.next
            return temp


    def display(self):
        runner = self.head
        # print(runner)
        while runner != None:

            runner = runner.next
        return self

    def front(self):
        if self.head == None:
            return None
        else:
            return self.head.value


    def contains(self, valueInput):
        #code here to return a boolean if value in any of the nodes
        #examine the values inside each node and compare
        runner = self.head
        #while runner is pointing to a node
        while runner != None:
            # print(runner)
            # print(valueInput)
            if runner.value == valueInput:
                return True
            runner = runner.next
        return False

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def size(self):
        total = 0
        runner = self.head
        while runner != None:
            total += 1
            runner = runner.next
        # print(total)
        return total


q1 = Queue()
q2= Queue()
q1.enqueue("l").enqueue("o").enqueue("l")
q2.enqueue("h").enqueue("e").enqueue("l").enqueue('o')

def isPalindrome(queueInput):
    runner = queueInput.head
    cheatylist = []
    while runner != None:
        cheatylist.append(runner.value)
        runner=runner.next
    length = int(len(cheatylist)/2)
    for i in range(length):
        if cheatylist[i] != cheatylist[len(cheatylist)-i-1]:
            return False
    return True

print(q1)
print(q2)

isPalindrome(q1)
