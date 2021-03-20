#Challenge - https://www.geeksforgeeks.org/josephus-circle-using-circular-linked-list/


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.start = None

  def append(self, data):
    node = Node(data)
    self.insertEnd(node)

  def getNode(self, index, start):
    if self.start == None:
      return None
    temp = start
    for _ in range(index):
      temp = temp.next
    return temp

  def getPrevNode(self, refNode):
      if self.start == None:
        return None
      temp = self.start
      while temp.next != refNode:
        temp = temp.next
      return temp

  def insertAfter(self, refNode, newNode):
      newNode.next = refNode.next
      refNode.next = newNode

  def insertBefore(self, refNode, newNode):
      prevNode = self.getPrevNode(refNode)
      self.insertAfter(prevNode, newNode)

  def insertEnd(self, newNode):
      if self.start == None:
        self.start = newNode
        newNode.next = newNode
      else:
        self.insertBefore(self.start, newNode)

  def remove(self, node):
      if self.start.next == self.start:
        self.start = None
      else:
        prevNode = self.getPrevNode(node)
        prevNode.next = node.next
        if self.start == node:
          self.start = node.next


def node1(myList):
  if myList.start.next == myList.start:
    return True
  else:
    return False


def solution(myList, m):
  if myList.start == None:
    return None
  start = myList.start
  while not node1(myList):
    toRemove = myList.get_node(m - 1, start)
    start = toRemove.next
    myList.remove(toRemove)
  return myList.start.data


clist = LinkedList()
n = int(input('Length of circle : n = '))
m = int(input('Count to choose next : m = '))
for i in range(1, n + 1):
  clist.append(i)
ans = solution(clist, m)
print(ans)
