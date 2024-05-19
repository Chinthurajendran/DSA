class MaxHeap:
    def __init__(self):
        self.head = []
         
    def insert(self, element):
        self.head.append(element)
        self.bubble_up(len(self.head) - 1)
    
    def bubble_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.head[index] > self.head[parent_index]:
            self.head[index], self.head[parent_index] = self.head[parent_index], self.head[index]
            self.bubble_up(parent_index)
    
    def remove(self, element):
        index = self.head.index(element)
        if index == len(self.head) - 1:
            return self.head.pop()
        self.head[index] = self.head.pop()
        parent_index = (index - 1) // 2
        if index > 0 and self.head[index] > self.head[parent_index]:
            self.bubble_up(index)
        else:
            self.bubble_down(index)
    
    def bubble_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.head) and self.head[left] > self.head[largest]:
            largest = left
        
        if right < len(self.head) and self.head[right] > self.head[largest]:
            largest = right
        
        if largest != index:
            self.head[index], self.head[largest] = self.head[largest], self.head[index]
            self.bubble_down(largest)

# Testing the MaxHeap implementation
max_heap = MaxHeap()
max_heap.insert(5)
max_heap.insert(3)
max_heap.insert(8)
max_heap.insert(1)

# max_heap.remove(5)

print("Heap after extracting maximum:", max_heap.head)
