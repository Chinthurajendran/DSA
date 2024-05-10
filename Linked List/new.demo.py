class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class Linked_list:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print("List is ematy")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def after(self,data,x):
        n = self.head
        while n is None:
            if n.data == x:
                break
            n=n.ref
        if n is None:
            print("node is none")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def befor(self,data,x):
        if self.head is None:
            print("list is ematy")
            return
        
        if self.head == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is not None:
            print("node is none")
        else:
            new_node =Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def first_delete(self):
        if self.head is None:
            print("List is ematy")
        else:
            self.head = self.head.ref

    def end_delete(self):
        if self.head is None:
            print("List is ematy")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_list(self,x):
        if self.head is None:
            print("list is ematy")
            return
        
        if self.head == x:
            self.head = self.head.ref
            return
        
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("node is none")
        else:
            n.ref = n.ref.ref




data = Linked_list()

data.add(20)
data.add(50)

data.end(80)

data.after(150,20)

data.befor(800,50)

data.first_delete()
data.end_delete()

data.delete_list(20)

data.print_list()