stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()


print(stack[::-1])
print(stack)
print(stack[3:1:-1])


from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)


queue2 = deque()

queue2.append(5)
queue2.append(2)
queue2.append(3)
queue2.append(7)
queue2.pop()
queue2.append(1)
queue2.append(4)
queue2.pop()
print(queue)

