# Challenge - https://www.geeksforgeeks.org/exchange-first-last-node-circular-linked-list/


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Linkedlist:
  def __init__(self):
    self.start = None

  def replace(self):
    temp = self.start
    temp1 = None
    index = None
    if self.start == None:
      return
    else:
      while temp.next != None:
          index = temp
          temp = temp.next
      if self.start == temp:
        return
      elif self.start.next == temp:
        temp1 = self.start
        self.start = temp
        self.start.next = temp1
        temp1.next = None
      else:
        temp1 = self.start
        self.start = temp
        self.start.next = temp1.next
        index.next = temp1
        temp1.next = None

  def insert(self, value):
    newNode = Node(value)
    if self.start == None:
      self.start = newNode
    else:
      temp = self.start
      while temp.next != None:
        temp = temp.next
      temp.next = newNode

  def printList(self):
    if self.start == None:
      print('NULL')
    else:
      temp = self.start
      while temp != None:
        print(temp.data, end='->')
        temp = temp.next


llist = Linkedlist()
llist.insert(1)
llist.insert(2)
llist.insert(3)
llist.insert(4)
llist.insert(5)
llist.insert(6)
llist.printList()
print()
llist.replace()
llist.printList()
print()
