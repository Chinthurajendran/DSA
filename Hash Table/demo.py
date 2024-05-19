class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
    
class hash_table:
    def __init__(self,size):
        self.size = size
        self.table = [None]*size

    def hash_value(self,key):
        data = 0
        for char in key:
            data+= ord(char)
        return data % self.size
    
    def add(self,key,value):
        index = self.hash_value(str(key))

        if self.table[index] is None:
            self.table[index] = Node(key,value)
        else:
            node = self.table[index]
            while node.next is not None:
                node = node.next
            node.next = Node(key,value)

            
        
    def search(self,key):
        index = self.hash_value(str(key))

        node = self.table[index]

        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        return None 

    def display(self):
        for index,node in enumerate(self.table):
            print(f"{index}:",end=" ")
            while node is not None:
                print(f"[{node.key}:{node.value}]",end="-->")
                node = node.next
            print('None')

info = hash_table(10)
info.add(1, "Alice")
info.add(2, "Bob")
info.add(11, "Charlie")  # Collision with key 1
info.add(21, "David")    # Collision with key 1 and 11

info.display()