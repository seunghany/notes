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

class LinkedNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None

    def hasNext(self):
        return self.next is not None

class MyStack():
    def __init__(self) -> None:
        self.size = 0
        self.sentinel = LinkedNode(0)

    def push(self, x: int) -> None:
        newHead = LinkedNode(x)
        newHead.next = self.sentinel.next
        self.sentinel.next = newHead
        self.size += 1

    def top(self) -> int:
        return self.sentinel.next.val

    def pop(self):
        self.sentinel.next = self.sentinel.next.next
        self.size -= 1

    def getSize(self) -> int:
        return self.size

    def isEmpty(self) -> bool:
        return self.size == 0

    def __str__(self):
        temp = self.sentinel
        result = "sentinel -> "
        while temp.hasNext():
            temp = temp.next
            result += (str(temp.val) + " -> ")
        result += "None"
        return result

if __name__ == '__main__':
    stack = MyStack()
    print(stack)
    stack.push(5)
    print(stack)
    top = stack.top()
    print("top: ", top)
    print(stack.getSize())
    print(stack.isEmpty())
    stack.push(4)
    print(stack.top())
    stack.pop()
    print(stack.top())
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.push(1)
    print(stack)