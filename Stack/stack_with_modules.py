import collections
stack = collections.deque()
print(stack)
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)
stack.pop()
print(stack)
print(stack[-1])
print()


import queue
stack = queue.LifoQueue()
stack.put(10)
stack.put(20)
stack.put(30)
stack.get()

while not stack.empty():
    item = stack.get()
    print(item)

