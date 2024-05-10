import collections
queue = collections.deque()
queue.appendleft(10)
queue.appendleft(20)
queue.appendleft(30)
print(queue)
queue.pop()
print(queue)

new = collections.deque()
new.append(90)
new.append(80)
new.append(70)
new.append(60)
print(new)
new.popleft()
print(new)


import queue
list = queue.Queue()
list.put(100)
list.put(200)
list.put(300)
list.get()
while not list.empty():
    item = list.get()
    print(item)