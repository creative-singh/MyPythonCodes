# Challenge - Given 2 very very big numbers(10^1000) use doubly linked lists to perform operations on them(+,-,*,/).


class Node:
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None


class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def insertAtBeginning(self, data=10 ^ 1000):
    if self.head is not None:
      newNode = Node(data)
      newNode.next = self.head
      self.head.prev = newNode
      self.head = newNode
    else:
      newNode = Node(data)
      self.head = newNode
      self.size = self.size+1

  def pop(self):
    if self.head is None:
      return self.head
    self.size -= 1
    data = self.head.data
    self.head = self.head.next
    return data


def addList(L1, L2):
  num1 = sum([L1[i]*(10**i) for i in range(len(L1)-1, -1, -1)])
  num2 = sum([L2[i]*(10**i) for i in range(len(L2)-1, -1, -1)])
  return num1 + num2


def multi(L1, L2):
  num1 = sum([L1[i]*(10**i) for i in range(len(L1)-1, -1, -1)])
  num2 = sum([L2[i]*(10**i) for i in range(len(L2)-1, -1, -1)])
  return num1 * num2


def subt(L1, L2):
  num1 = sum([L1[i]*(10**i) for i in range(len(L1)-1, -1, -1)])
  num2 = sum([L2[i]*(10**i) for i in range(len(L2)-1, -1, -1)])
  return num1 - num2


dList = DoublyLinkedList()
dList.insertAtBeginning(5)
dList.insertAtBeginning(4)
dList.insertAtBeginning(3)
dList.insertAtBeginning(2)
dList.insertAtBeginning(1)
lst = []
while True:
  data = dList.pop()
  if data is None:
    break
  lst.append(data)
print('List 1 :', *lst)
dList2 = DoublyLinkedList()
dList2.insertAtBeginning(1)
dList2.insertAtBeginning(2)
dList2.insertAtBeginning(3)
dList2.insertAtBeginning(4)
dList2.insertAtBeginning(5)
lst2 = []
while True:
  data = dList2.pop()
  if data is None:
    break
  lst2.append(data)
print('List 2 :', *lst2)
print()
total = addList(lst, lst2)
print('Addition :', ' '.join(str(total)))
sub = subt(lst, lst2)
print('Subtration :', ' '.join(str(sub)))
mul = multi(lst, lst2)
print('Multiplication :', ' '.join(str(mul)))
