class TreeNode():
    def __init__(self, x: int) -> None:
        self.val = x
        self.left = None
        self.right = None

class BST():
    def __init__(self, root: TreeNode) -> None:
        self.root = root

    def __searchHelp(self, ,curNode: TreeNode, x: int) -> TreeNode:
        # (1) Base cases
        if not curNode:
            return None
        if x == curNode.val:
            return curNode

        # (2) Recursive cases
        if x < curNode.val:
            return self.__searchHelp(curNode.left, x)
        else:
            return self.__searchHelp(curNode.right, x)

    def search(self, x: int) -> TreeNode:
        return self.__searchHelp(self.root, x)

    def __insertHelp(self, curNode: TreeNode, x: int) -> TreeNode:
        # (1) Base case
        if not curNode:
            return TreeNode(x)
        if x == curNode.val:
            return curNode

        # (2) Recursive case
        if x < curNode.val:
            curNode.left = self.__insertHelp(curNode.left, x)
        else:
            curNode.right = self.__insertHelp(curNode.right, x)

        return curNode

    def insert(self, x: int) -> None:
        self.root = self.__insertHelp(self.root, x)

    def __findMax(self, curNode: TreeNode) -> int:
        # (1) Base case
        if not curNode.right:
            return curNode.val
        # (2) Recursive case
        else:
            return self.__findMax(curNode.right)

    def __deleteHelp(self, curNode: TreeNode, x: int) -> TreeNode:
        # (1) Base case
        if not curNode:
            return None

        # (2) Recursive cases
        if x < curNode.val:
            curNode.left = self.__deleteHelp(curNode.left, x)
        elif x > curNode.val:
            curNode.right = self.__deleteHelp(curNode.right, x)

        else:  # x == curNode.val: We should delete this node!!
            # (1) No child
            # if curNode.left == None and curNode.right == None:
            #    return None

            # (2) One child
            # elif curNode.left == None and curNode.right:
            #    return curNode.right
            # elif curNode.left and curNode.right == None:
            #    return curNode.left

            if curNode.left == None:
                return curNode.right
            elif curNode.right == None:
                return curNode.left

            # (3) Two children
            else:
                leftLargest = self.__findMax(curNode.left)
                curNode.left = self.__deleteHelp(curNode.left, leftLargest)
                curNode.val = leftLargest

        return curNode

    def delete(self, x: int) -> None:
        self.root = self.__deleteHelp(self.root, x)