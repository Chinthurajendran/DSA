class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class linked_list:
    def __init__(self):
        self.head = None
    
    def dispaly(self):
        if self.head is None:
            print("List empty")
        else:
            node = self.head
            while node is not None:
                print(node.data)
                node = node.ref
    def start(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head= new_node
    
    def end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.ref is not None:
                node = node.ref
            node.ref = new_node
    
    def after(self,data,x):
        node = self.head
        while node is not None:
            if node.data == x:
                break
            node = node.ref
        if node is None:
            print("Value not found")
        else:
            new_node = Node(data)
            new_node.ref = node.ref
            node.ref = new_node


data = linked_list()
data.start(10)
data.end(100)
data.after(50,10)
data.dispaly()