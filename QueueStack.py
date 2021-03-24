# Challenge - Implement Queues using Stacks


class Stack:
  def __init__(self, maxSize=100):
    self.maxSize = maxSize
    self.top = -1
    self.stackData = []
    self.stackb = []

  def push(self, data):
    if self.maxSize > self.top:
      self.stackData.append(data)
      self.top += 1
    else:
      print('Stack is full')

  def peek(self):
    if self.top < 0:
      print('None')
    else:
      print(self.stackData[-1])

  def botton(self):
    print(self.stackData[0])

  def pop(self):
    if not self.stackb:
      while self.stackData:
        self.stackb.append(self.stackData.pop())
    print(self.stackb.pop())
    print('After dequeue : ',end='')
    print(*self.stackb)

  def isEmpty(self):
    if self.top < 0:
      print('True')
    else:
       print('False')

  def printStack(self):
    stackList = self.stackData
    if self.top < 0:
      print('List is empty')
      return
    else:
      print(*stackList)


class Queue:
  def __init__(self):
    self.stack = Stack()

  def enqueue(self, data):
    self.stack.push(data)

  def dequeue(self):
    self.stack.pop()

  def frontElem(self):
    self.stack.botton()

  def rearElem(self):
    self.stack.peek()

  def isEmpty(self):
    self.stack.isEmpty()

  def printQueue(self):
    self.stack.printStack()


que = Queue()
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
que.enqueue(4)
que.enqueue(5)
print('Queue is : ',end='')
que.printQueue()
print('Front element : ',end='')
que.frontElem()
print('Rear element : ',end='')
que.rearElem()
print('Dequeue element : ',end='')
que.dequeue()
print('Whether empty : ',end='')
que.isEmpty()
