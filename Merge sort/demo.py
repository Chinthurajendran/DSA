class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.ref = None

class hash_table:
    def __init__(self,size):
        self.size = size
        self.table = [None]*size
    
    def hash_value(self,key):
        return hash(key)%self.size
    
    def insert(self,key,value):
        index = self.hash_value(str(key))
        if self.table[index] is None:
            self.table[index] = Node(key,value)
        else:
            node = self.table[index]
            while node.ref is not None:
                node = node.ref
            node.ref =self.table[index]
    
    def search(self,key):
        index = self.hash_value(str(key))
        node = self.table[index]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.ref
        return None
    
    def display(self):
        for index,node in enumerate(self.table):
            print(f'index :{index}',end=" ")
            while node is not None:
                print(f'{[node.key],[node.value]}',end=" ")
                node = node.ref
            print('None')

data = hash_table(10)
data.insert(1,'chinthu')
data.insert(2,'sanju')
print(data.search(1))
data.display()
