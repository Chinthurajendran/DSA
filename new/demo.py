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
        return data%self.size
    
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
    
    def dispaly(self):
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
print(info.search(1))

info.dispaly()


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range (i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j]=arr[j],arr[i]

arr = [12, 11, 13, 5, 6]
bubble_sort(arr)
print("Bubble sorted array is:", arr)

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index =  j
        arr[i],arr[min_index]=arr[min_index],arr[i]
            
arr = [12, 11, 13, 5, 6]
selection_sort(arr)
print("Selection sorted array is:", arr)

def insertion_sort(arr):
    for i in range(1,len(arr)):
        j = i
        while arr[j-1] > arr[j] and j >0 :
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1



arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Insertion sorted array is:", arr)