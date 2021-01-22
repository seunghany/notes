class LinkedNode:

    def __init__(self, x: int):
        self.val = x
        self.next = None

class SLList():
    def __init__(self) -> None:
        self.first = None  # head
        self.size += 1

    def addFirst(self, x: int) -> None:
        newFirst = LinkedNode(x)
        newFirst.next = newFirst
        self.first = newFirst
        self.size +=1

    def getFirst(self) -> int:
        return self.first.val

    def getSize(self) -> int:
        return self.size

    def hasNext(self):
        # return True if LinkedList has next Node
        # return False otherwise
        return self.next is not None