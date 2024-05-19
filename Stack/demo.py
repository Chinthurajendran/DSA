# import collections
# stack =  collections.deque()
# stack.append(10)
# stack.append(20)
# stack.append(30)
# print(stack)
# stack.pop()
# print(stack)


import queue
stack = queue.LifoQueue()
stack.put(60)
stack.put(70)
stack.put(80)
stack.get()
while not stack.empty():
    items = stack.get()
    print(items)

import collections
queu = collections.deque()
queu.appendleft(10)
queu.append(20)
queu.append(30)
print(queu)
queu.pop()
print(queu)

import queue
new = queue.Queue()
new.put(100)
new.put(200)
new.get()
while not new.empty():
    items = new.get()
    print(items)