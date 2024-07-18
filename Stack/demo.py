class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class stack:
    def __init__(self):
        self.top = None
    
    def insert(self,data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.ref = self.top
            self.top = new_node
    
    def remove(self):
        if self.top is None:
            print("List is empty")
        else:
            self.top = self.top.ref
    
    def dispaly(self):
        if self.top is None:
            print("List is none")
        else:
            node= self.top
            while node is not None:
                print(node.data)
                node = node.ref

data = stack()
data.insert(10)
data.insert(20)
data.insert(30)
data.remove()
data.dispaly()