class MinHeap:
    def __init__(self):
        self.head = []
    
    def insert(self,element):
        self.head.append(element)
        self.bubble_up(len(self.head)-1)
    
    def bubble_up(self,index):
        parant_index = (index-1)//2
        if index > 0 and self.head[index] > self.head[parant_index]:
            self.head[index],self.head[parant_index] = self.head[parant_index],self.head[index]
            self.bubble_up(parant_index)
    
    def remove(self,elemnt):
        index = self.head.index(elemnt)
        if index == len(self.head)-1:
            return self.head.pop()
    
        self.head[index] = self.head.pop()
        parant_index = (index-1)//2
        if index > 0 and self.head[index] > self.head[parant_index]:
            self.bubble_up(index)
        else:
            self.bubble_down(index)
    
    def bubble_down(self,index):
        smallest = index
        left = 2*index+1
        right = 2*index+2

        if left < len(self.head) and self.head[left] > self.head[smallest]:
            smallest = left
        
        if right < len(self.head) and self.head[right] > self.head[smallest]:
            smallest = right
        
        if smallest != index:
            self.head[index],self.head[smallest] = self.head[smallest],self.head[index]
            self.bubble_down(smallest)
 

min_heap = MinHeap()
min_heap.insert(5)
min_heap.insert(3)
min_heap.insert(8)
min_heap.insert(1)

# min_heap.remove(5)

print("Heap after extracting minimum:", min_heap.head)