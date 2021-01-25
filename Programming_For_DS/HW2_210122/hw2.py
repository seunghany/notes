# Please complete below function
def HW2_3(l: ListNode) -> ListNode:
    """
        Input: First node of  a linked list
        Output: First node of reverse linked list
    """
    stack = MyStack()
    stack.push(l.val)
    while l.next:
        l = l.next
        stack.push(l.val)
    print(stack)
    result = stack.pop()
    temp = result
    while stack.size >= 0:
        temp.next = stack.pop()
    return result
