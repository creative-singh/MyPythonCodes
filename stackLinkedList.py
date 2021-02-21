#Challenge - Implement Stack using a linked list

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.top = None

  def push(self, data):
    if self.top == None:
      self.top = Node(data)
    else:
      newNode = Node(data)
      newNode.next = self.top
      self.top = newNode

  def peek(self):
    if self.top == None:
      return None
    else:
      peek = self.top.data
      print(peek)

  def pop(self):
    if self.top == None:
      return True
    else:
      pop = self.top.data
      self.top = self.top.next
      print(pop)

  def isEmpty(self):
    if self.top == None:
      return True
    else:
      print('False')

  def printStack(self):
    stackList = self.top
    if self.top == None:
      print('List is empty')
      return
    while stackList != None:
      print(stackList.data, end=' ')
      stackList = stackList.next


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print('Full Stack : ',end='')
stack.printStack()
print()
print('Stack Top : ',end='')
stack.peek()
print('Popping Element : ',end='')
stack.pop()
print('Stack After Popped : ',end='')
stack.printStack()
print()
print('Whether Empty : ',end='')
stack.isEmpty()
print()
