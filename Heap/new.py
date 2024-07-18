class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def delete_max(self):
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()

        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_val

    def _heapify_up(self, index): #insert
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            # Swap current index with parent
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            # Move up to the parent level
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index): #del
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        # Compare with left child
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        # Compare with right child
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        # If largest is not root
        if largest != index:
            # Swap root with largest element
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            # Recursively heapify the affected sub-tree
            self._heapify_down(largest)

    def print_heap(self):
        print("Max Heap:", self.heap)


# Example usage:
max_heap = MaxHeap()
max_heap.insert(5)
max_heap.insert(3)
max_heap.insert(17)
max_heap.insert(10)
max_heap.insert(84)

max_heap.print_heap()

print("Deleting max element:", max_heap.delete_max())
max_heap.print_heap()