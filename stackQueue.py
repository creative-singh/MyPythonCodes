# Challenge - Implement Stacks using Queues


class Queue:
  def __init__(self, maxSize=100):
    self.maxSize = maxSize
    self.queue = []
    self.front = self.rear = -1

  def enqueue(self, data):
    if self.rear < self.maxSize:
      self.queue.append(data)
      self.rear += 1
      if self.front == -1:
        self.front = 0
    else:
      print('List is full')

  def dequeue(self):
    if self.rear == self.front == -1:
      return None
    else:
      elem = self.queue.pop(self.rear)
      if self.rear == 0:
        self.front = self.rear = -1
      else:
        self.rear -= 1
      print(elem)

  def frontElem(self):
    if self.front != -1:
      print(self.queue[self.front])
    return None

  def rearElem(self):
    if self.rear != -1:
      print(self.queue[self.rear])
    return None

  def isEmpty(self):
    if self.front == self.rear == -1:
      print('True')
    else:
      print('False')

  def printQueue(self):
    queList = self.queue
    if self.front == self.rear == -1:
      print('Queue is empty')
    else:
      print(*queList)


class Stack:
  def __init__(self):
    self.queue = Queue()

  def push(self, data):
    self.queue.enqueue(data)

  def peek(self):
    self.queue.rearElem()

  def pop(self):
    self.queue.dequeue()

  def isEmpty(self):
    self.queue.isEmpty()

  def printStack(self):
    self.queue.printQueue()


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print('Stack is : ',end='')
stack.printStack()
print('Stack top : ',end='')
stack.peek()
print('Popping element : ',end='')
stack.pop()
print('after popped : ',end='')
stack.printStack()
print('Whether empty : ',end='')
stack.isEmpty()
