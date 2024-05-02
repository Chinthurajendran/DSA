class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class Linked_list:
    def __init__(self): 
        self.head = None
    def Print_ll(self):
        if self.head is None:
            print("list is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x==n.data:
                break
            n= n.ref
        if n is None:
            print("node is not present in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_befor(self,data,x):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def list_empty(self,data):
        if self.head is not None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("List is not empty")
        
    def first_delete(self):
        if self.head is None:
            print("List is empaty")
        else:
            self.head = self.head.ref
        
    def end_delete(self):
        if self.head is None:
            print("List is empaty")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def after_delete(self,x):
        if self.head is None:
            print("List is ematy")
            return
        if self.head.data == x:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("not match")
        else:
            n.ref = n.ref.ref




LL1 = Linked_list()
LL1.add_begin(30)
LL1.add_begin(50)

# LL1.add_end(100)
# LL1.add_after(5,20)
# LL1.add_befor(900,20)
# LL1.list_empty(8520)
# LL1.first_delete()
# LL1.end_delete()
# LL1.after_delete(30)

LL1.after_delete(60)

LL1.Print_ll()