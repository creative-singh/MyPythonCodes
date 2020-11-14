# Challenge - https://www.geeksforgeeks.org/reverse-a-linked-list/


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Linkedlist:
  def __init__(self):
    self.start = None

  def reverse(self):
      prev = None
      temp = self.start
      while temp != None:
        next = temp.next
        temp.next = prev
        prev = temp
        temp = next
      self.start = prev

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
llist.reverse()
llist.printList()
print()
