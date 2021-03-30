# Challenge - Reverse a Doubly linked list using recursion


class DoubleNode:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None


class DoublyLinkedList:
  def __init__(self):
    self.head = None

  def insertAtBeginning(self, data):
    if self.head is not None:
      newNode = DoubleNode(data)
      newNode.next = self.head
      self.head.prev = newNode
      self.head = newNode
    else:
      newNode = DoubleNode(data)
      self.head = newNode

  def reverse(self):
    if self.head is None or self.head.next is None:
      return self.head
    currentNode = self.head

    def reverseNode(node):
      if node is None:
        return
      if node.next is None:
        node.prev = None
        return node
      newHead = reverseNode(node.next)
      newNode = node.next
      temp = newNode.next
      newNode.prev = temp
      newNode.next = node
      node.next = None
      return newHead
    self.head = reverseNode(currentNode)

  def printList(self):
    if self.head is None:
      print('List is empty')
    currentNode = self.head
    while True:
      if currentNode is None:
        break
      print(currentNode.data, end=' <-> ')
      currentNode = currentNode.next


dList = DoublyLinkedList()
dList.insertAtBeginning(5)
dList.insertAtBeginning(4)
dList.insertAtBeginning(3)
dList.insertAtBeginning(2)
dList.insertAtBeginning(1)
print('Input : ')
print(dList.printList())
print('Output : ')
dList.reverse()
print(dList.printList())
