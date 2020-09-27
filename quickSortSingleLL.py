#Challenge - https://www.geeksforgeeks.org/quicksort-on-singly-linked-list/


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def insert(self, data):
    self.length += 1
    new = Node(data)
    if self.tail is None:
      self.head = self.tail = new
    else:
      self.tail.next = new
      self.tail = new

  def pop(self):
    if self.head is None:
      return self.head
    self.length -= 1
    data = self.head.data
    self.head = self.head.next
    return data

  def show(self, head, tail):
    lst = []
    if head is None:
      print(lst)
      return
    while True:
      if head.data is not None:
        lst.append(head.data)
      if head is tail:
        break
      head = head.next
    print(lst)

  def quickSort(self, head, tail):
    if head is tail:
      return head, tail
    hlt = Node(None)
    tlt = hlt
    heq = Node(None)
    teq = heq
    hgt = Node(None)
    tgt = hgt
    pivot = head
    curr = head
    end = tail.next
    while curr is not end:
      if curr.data < pivot.data:
        tlt.next = curr
        tlt = curr
      elif curr.data == pivot.data:
        teq.next = curr
        teq = curr
      else:
        tgt.next = curr
        tgt = curr
      curr = curr.next
    heq = heq.next
    if hlt is tlt:
      hlt = heq
      tlt = heq
    else:
      hlt = hlt.next
      hlt, tlt = self.quickSort(hlt, tlt)
      tlt.next = heq
    if hgt is tgt:
      hgt = teq
      tgt = teq
    else:
      hgt = hgt.next
      hgt, tgt = self.quickSort(hgt, tgt)
      teq.next = hgt
    return(hlt, tgt)

  def sort(self):
    if self.head == None:
      return
    self.head, self.tail = self.quickSort(self.head, self.tail)
    self.tail.next = None
    return

  def printList(self):
    if self.head is None:
      print('List is empty')
    current_node = self.head
    while True:
      if current_node is None:
        break
      print(current_node.data, end=' ')
      current_node = current_node.next


linkedList = LinkedList()
linkedList.insert(12)
linkedList.insert(9)
linkedList.insert(3)
linkedList.insert(2)
linkedList.insert(8)
linkedList.insert(6)
linkedList.insert(1)
linkedList.insert(4)
linkedList.insert(7)
linkedList.insert(5)
linkedList.insert(0)
linkedList.insert(10)
print('Unsorted list : ')
print(linkedList.printList())
linkedList.sort()
lst = []
while True:
  data = linkedList.pop()
  if data is None:
    break
  lst.append(data)
print('Sorted list : ')
print(*lst, end=' None')
print()
