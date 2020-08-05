# https://www.geeksforgeeks.org/pairwise-swap-elements-of-a-given-linked-list/
'''
Input : 1->2->3->4->5->6->NULL
Output : 2->1->4->3->6->5->NULL

Input : 1->2->3->4->5->NULL
Output : 2->1->4->3->5->NULL
'''


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Linkedlist:
  def __init__(self):
    self.start = None

  def pairChange(self):
    temp = self.start
    if temp == None:
      return
    else:
      while (temp != None and temp.next != None):
        temp.data, temp.next.data = temp.next.data, temp.data
        temp = temp.next.next

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
        print(temp.data, end=' -> ')
        temp = temp.next


myllist = Linkedlist()
myllist.insert(1)
myllist.insert(2)
myllist.insert(3)
myllist.insert(4)
myllist.insert(5)
myllist.insert(6)
myllist.printList()
print()
myllist.pairChange()
myllist.printList()
print()
