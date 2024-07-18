from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.q = deque()
    
    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    
    def pop(self):
        if not self.q:
            return None
        return self.q.popleft()
    
    def top(self):
        if not self.q:
            return None
        return self.q[0]
    
    def empty(self):
        return len(self.q) == 0

# Example usage
stack = StackUsingQueue()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.top())  # Output: 3
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2
print(stack.empty())  # Output: False
print(stack.pop())  # Output: 1
print(stack.empty())  # Output: True
