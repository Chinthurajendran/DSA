class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class print_list:
    def __init__(self):
        self.head = None
    
    def print_data(self):
        if self.head is None:
            print("the list is ematy")
        else:
            n = self.head
            while n is not None:
                print(n.data,end=" ")
                n = n.ref

    def add(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def duplicate(self):
        current = self.head
        while current is not None:
            runner = current
            while runner.ref is not None:
                if runner.ref.data == current.data:
                    runner.ref = runner.ref.ref
                else:
                    runner = runner.ref
            current = current.ref


data = print_list()
lst = [10,20,10,30,50,60,50,30,40]
lst.sort()
for i in lst:
    data.add(i)

data.duplicate()

data.print_data()
