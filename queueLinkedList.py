# Challenge - Implement Queue Using a linked list
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Queue:
  def __init__(self):
    self.front = None
    self.rear = None

  def enqueue(self, data):
    newNode = Node(data)
    if self.rear == None:
      self.front = newNode
      self.rear = newNode
      return
    self.rear.next = newNode
    self.rear = newNode

  def dequeue(self):
    if self.front == None:
      self.rear == None
      return None
    else:
      elem = self.front
      self.front = elem.next

  def frontElem(self):
    if self.front != None:
      front = self.front.data
      print(front)
    return None

  def rearElem(self):
    if self.rear != None:
      rear = self.rear.data
      print(rear)
    return None

  def isEmpty(self):
    if self.front == self.rear == None:
      print('True')
    else:
      print('False')

  def printQueue(self):
    queList = self.front
    if self.front == None:
      print('Queue is empty')
    while queList != None:
      print(queList.data, end=' ')
      queList = queList.next


que = Queue()
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
que.enqueue(4)
que.enqueue(5)
print('Queue Is : ', end='')
que.printQueue()
print()
print('Front Element : ', end='')
que.frontElem()
print('Rear Element : ', end='')
que.rearElem()
que.dequeue()
print('After Dequeue : ', end='')
que.printQueue()
print()
print('Whether Empty : ', end='')
que.isEmpty()
