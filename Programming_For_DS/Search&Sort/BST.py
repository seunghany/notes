class TreeNode():
    def __init__(self, value:int):
        self.val = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def search(self, target: int):
        return self.__searchHelp(self.root, target)

    def __searchHelp(curr, target):
        if not curr:
            return None
        if target == curr.val:
            return curr
        elif target< curr.val:
            return self.__searchHelp(curr.left, target)
        else:
            return self.__searchHelp(curr.right, target)

    def insert(self, insertValue: int):
        self.root = __self.insertHel(self.root, insertValue)

    def __insertHelp(curr, insertValue):
        if not curr:  # same as curr is None:
            return TreeNode(insertValue)
        if insertValue < curr.val:
            curr.left = self.__inserHelp(curr.left, insertValue)
        else:
            curr.right = self.__inserHelp(curr.right, insertValue)

    def delete(self, deleteValue: int):
        self.root = __helpDelete(self.root, deleteValue)

    def __helpDelete(curr, deleteValue):
        if not curr:
            return None
        # 못 찾고 끝에 도착했을때

        if curr.isLeafNode:
            # no child
            return None
        elif not curr.left and curr.right:
            # has left node but not right
        elif curr.left and not curr.right:
            # has no left but right
        else:
            # has both left and right
            # maybe I just need this

    def isLeafNode(curr):
        return not (curr.left or curr.right)
        # Case 1: Delete a leaf node (no child)
# Search the node using its key value
# Simply cut the parent’s link
# Then the target node is gone

