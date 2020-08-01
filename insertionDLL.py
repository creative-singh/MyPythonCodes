class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def getNode(data):
    newNode = Node(0)
    newNode.data = data
    newNode.prev = newNode.next = None
    return newNode


def sortedInsert(headRef, newNode):
    current = None
    if (headRef == None):
        headRef = newNode
    elif ((headRef).data >= newNode.data):
        newNode.next = headRef
        newNode.next.prev = newNode
        headRef = newNode
    else:
        current = headRef
        while (current.next != None and
               current.next.data < newNode.data):
            current = current.next

        newNode.next = current.next
        if (current.next != None):
            newNode.next.prev = newNode

        current.next = newNode
        newNode.prev = current

    return headRef


def insertionSort(headRef):
    sorted = None
    current = headRef
    while (current != None):

        next = current.next

        current.prev = current.next = None
        sorted = sortedInsert(sorted, current)
        current = next
    head_ref = sorted

    return headRef


def printList(head):

    while (head != None):
        print(head.data, end=" ")
        head = head.next


def push(headRef, newData):

    newNode = Node(0)

    newNode.data = newData

    newNode.next = (headRef)
    newNode.prev = None

    if ((headRef) != None):
        (headRef).prev = newNode

    (headRef) = newNode
    return headRef


if __name__ == "__main__":

    head = None
    head = push(head, 9)
    head = push(head, 3)
    head = push(head, 5)
    head = push(head, 10)
    head = push(head, 12)
    head = push(head, 8)

    print('Doubly Linked List Before Sorting')
    printList(head)

    head = insertionSort(head)

    print("Doubly Linked List After Sorting")
    printList(head)
