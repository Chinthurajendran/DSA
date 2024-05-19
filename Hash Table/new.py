class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        

    def hash_value(self, key):
        # Hash function to calculate the index
        return hash(key) % self.size

    def add(self, key, value):
        index = self.hash_value(str(key))
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            # Append the new node to the end of the linked list
            node = self.table[index]
            while node.next is not None:
                node = node.next
            node.next = Node(key, value)

    def get_data(self, key):
        index = self.hash_value(str(key))
        node = self.table[index]

        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def display(self):
        for index, node in enumerate(self.table):
            print(f"Index {index}: ", end="")
            while node is not None:
                print(f"[{node.key}: {node.value}]", end=" -> ")
                node = node.next
            print("None")

# Example usage
info = HashTable(10)
info.add(1,"march 6")
info.add(2,"march 17")
info.add(3,"march 18")
info.add(4,"march 19")
info.add(5,"march 20")
info.add(6,"march 21")
info.add(7,"march 22")

info.display()
