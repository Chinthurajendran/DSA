class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
    
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def insert(self,data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.ref = new_node
        self.rear = new_node
    
    def remove(self):
        if self.front is None:
            print("List is empty")
        else:
            self.front = self.front.ref
        if self.front is None:
            self.rear = None
    
    def display(self):
        if self.front is None:
            print("list is empty")
        else:
            node = self.front
            while node is not None:
                print(node.data)
                node = node.ref

data = Queue()
data.insert(10)
data.insert(20)
data.insert(30)
data.remove()
data.display()