# Implement stack by using single-linked list of LinkedNodes
# class LinkedNode():
#          def __init__(self, x: int) -> None:
#                    self.val = x
#                    self.next = None
#
# class myStack() has four methods
# push(x): Add a LinkedNode that has val = x to myStack
# pop: Remove the most recently added LinkedNode from myStack
# top: Return val of the most recently added LinkedNode
# getSize: Return the number of LinkedNodes in myStack
# isEmpty: Return True if myStack is empty, or False otherwise.

class LinkedNode():
    def __init__(self, x: int) -> None:
        self.val = x
        self.next = None

    def hasNext(self):
        # return True if LinkedList has next Node
        # return False otherwise
        return self.next is not None

class MyQueue():
    """
    First in First Out FIFO Queue
    """
    def __init__(self) -> None:
        self.size = 0
        self.sentinel = LinkedNode(0)

    def enqueue(self, x) -> None:
        # push(x): Add a LinkedNode that has val = x to myQueue
        # Simple method
        # if self.size == 0:
        #     self.head = LinkedNode(x)  # head 가 있을 경우
        temp = self.sentinel
        while temp.hasNext():
            temp = temp.next
        temp.next = LinkedNode(x)
        self.size += 1

    def dequeue(self):
        # pop: Removes the lastly added LinkedNode from myQueue
        if self.size < 1:
            pass
        elif self.size == 1:
            self.size -= 1
            self = None
        else:  # self. size >= 2
            temp = self.sentinel
            while temp.hasNext() and temp.next.hasNext():
                temp = temp.next
            temp.next = None
            self.size -= 1

    def peek(self):
        # top: Return val of the most recently added LinkedNode
        if self.size == 0:
            return "This LinkedNode is Empty"
        # elif self.size == 1:
        #     return self.val
        else:  # size >= 2
            temp = self.sentinel
            while temp.hasNext():
                temp = temp.next
            return temp.val

    def getSize(self) -> int:
        # getSize: Return the number of LinkedNodes in myStack
        return self.size

    def isEmpty(self) -> bool:
        # isEmpty: Return True if myStack is empty, or False otherwise.
        return self.size == 0

if __name__ == '__main__':
    x = MyQueue()
    x.enqueue(5)
    print(x.peek())

