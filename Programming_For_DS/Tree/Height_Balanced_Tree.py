class HBT():
    """Height Balanced Tree
    def:
    A non empty binary tree T is balanced if:
    1) left subtree of T is balanced if
    2) right subtree of T is balanced if
    3) The difference between heights of left subtree and right subtree is not more than 1
    eg)
     A        Balanced Tree
   /   \
  B     C
 /     / \
D     E   F
     /
    G

     A       Not Balanced Tree
   /   \
  B     C   <-- difference = 2
 /     /
D     E
     /
    G
    """
    # step 1 insert

    def insert(self, newNode):
        self.root = self.insertHelp(self, self.root, newNode)


    def insertHelp(self, curNode, newNode):
        # if Tree is empty
        if self.root == None:
            self.root = newNode

        if not curNode:
            return newNode


class TreeNode():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right