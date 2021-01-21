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
    def __init__(self, x: int, size=1) -> None:
        self.val = x
        self.next = None
        self.size = size

    def push(self, x) -> None:
        # push(x): Add a LinkedNode that has val = x to myStack
        if self.size == 0:
            self = LinkedNode(x)  # 이게 왜 안되는지 궁금
        else:
            temp = self
            while temp.hasNext():
                temp = temp.next
            temp.next = LinkedNode(x)
        self.size += 1

    def pop(self):
        # pop: Remove the most recently added LinkedNode from myStack
        if self.size == 0:
            pass
        elif self.size == 1:
            self.size -= 1
            self = None
        else:  # self. size >= 2
            temp = self
            while temp.hasNext() and temp.next.hasNext():
                temp = temp.next
            temp.next = None
            self.size -= 1

    def top(self):
        # top: Return val of the most recently added LinkedNode
        if self.size == 0:
            return "This LinkedNode is Empty"
        elif self.size == 1:
            return self.val
        else:  # size >= 2
            temp = self
            while temp.hasNext():
                temp = temp.next
            return temp.val

    def getSize(self) -> int:
        # getSize: Return the number of LinkedNodes in myStack
        return self.size

    def isEmpty(self) -> bool:
        # isEmpty: Return True if myStack is empty, or False otherwise.
        return self.size == 0

    def hasNext(self):
        # return True if LinkedList has next Node
        # return False otherwise
        return self.next is not None
