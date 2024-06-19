class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class linked_list:
    def __init__(self):
        self.head = None
    
    def print_all(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    
    def start(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    
    def end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n .ref is not None:
                n = n.ref
            n.ref = new_node
    
    def after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Value not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def befor(self,data,x):
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n =self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n is None:
            print("value not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def delete_start(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.ref
    
    def delete_end(self):
        if self.head is None:
            print("list is empty")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
    
    def delete_value(self,x):
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == x:
            self.head = self.head.ref
            return
        
        n = self.head
        while n.ref.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Value is not found")
        else:
            n.ref = n.ref.ref
        
    
        

list = linked_list()
list.start(10)
list.start(20)
list.end(100)
list.after(75,10)
list.befor(85,10)
list.delete_start()
list.delete_end()
list.delete_value(10)
list.print_all()