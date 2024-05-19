class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, element):
        self.heap.append(element)
        self._bubble_up(len(self.heap) - 1)

    def remove(self, element):
        index = self.heap.index(element)
        # print(index)
        # print(len(self.heap))
        if index == len(self.heap) - 1:
            return self.heap.pop()
        # Swap with the last element and remove it
        self.heap[index] = self.heap.pop()
        print(self.heap[index])
        
        parent_index = (index - 1) // 2
        # Restore heap property
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self._bubble_up(index)
        else:
            self._bubble_down(index)
    
    def _bubble_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._bubble_up(parent_index)

    def _bubble_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._bubble_down(smallest)

# Example usage
min_heap = MinHeap()
min_heap.insert(5)
min_heap.insert(3)
min_heap.insert(8)
min_heap.insert(1)

print("Heap:", min_heap.heap)

print("Heap after extracting minimum:", min_heap.heap)

min_heap.remove(1)
print("Heap after removing 5:", min_heap.heap)
