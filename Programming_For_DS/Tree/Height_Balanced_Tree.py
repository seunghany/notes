class TreeNode():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        self.bf = 0  # balance factor  -> left.height - right.height
class HBT():
    """Height Balanced Tree
    # balanced tree: One whose subtrees differ in height by at most 1 and are themselves balanced.
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
    def __init__(self, root = None):
        self.root = root

    def rotateRight(self):
        pass
        # clockwise rotation
        # left child becomes parent
        # original root becomes right child node
        # original left child's right subtree is now attatched to left of new right tree
    def height(self, root: TreeNode) -> int:
        '''
        Recieves TreeNode as a parameter
        and returns the height of the node.
        '''
        if root is None:
            return 0
        else:
            return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root: TreeNode) -> bool:
        """
        Recieves TreeNode (root) as a parameter and
        returns true if tree is balanced and false otherwise
        """
        if root is None:
            return True

        lh = self.height(root.left)  # left height
        rh = self.height(root.right)  # right height
        if abs(lh-rh) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False

    # step 1 insert
    def insert(self, newVal: int) -> None:
        """
        Recieves new integer value and adds a new tree node to the root
        """
        self.root = self.insertHelp(self.root, newVal)
        if self.isBalanced(self.root):
            print("Balanced")
        else:
            print("Not Balanced")
            # 만약 unbalanced 하다면 rotation 필요
            # Right Right	==> Z is a right	child of its parent X and BF(Z) ≥ 0
            # Left Left	==> Z is a left	child of its parent X and BF(Z) ≤ 0
            # Right Left	==> Z is a right	child of its parent X and BF(Z) < 0
            # Left Right	==> Z is a left	child of its parent X and BF(Z) > 0

            # And the rebalancing is performed differently:
            #
            # Right Right	==> X is rebalanced with a	simple	rotation rotate_Left
            # Left Left	==> X is rebalanced with a	simple	rotation rotate_Right
            # Right Left	==> X is rebalanced with a	double	rotation rotate_RightLeft
            # Left Right	==> X is rebalanced with a	double	rotation rotate_LeftRight
    def insertHelp(self, curNode, newVal):
        # Base Case
        if not curNode:  # 만약 끝에 도착한다면 새로운 노드 안착
            return TreeNode(newVal)
        if newVal == curNode.val:
            return curNode
        # recursive case
        if curNode.val < newVal:  # 숫자가 작으면 왼쪽으로
            curNode.left = self.insertHelp(curNode.left, newVal)
        else: # 숫자가 크면 오른쪽으로
            curNode.right = self.insertHelp(curNode.right, newVal)

        return curNode

    def rotation(self, curNode):
        # left rotation
        newRoot = curNode
        newRoot = newRoot.right
        oldLeft = newRoot.left  # 여기서 에러남
        newRoot.left = curNode
        curNode.right = oldLeft
        self.isBalanced(newRoot)
        return newRoot




if __name__ == '__main__':
    Tree = HBT()
    Tree.insert(5)
    Tree.insert(6)
    Tree.insert(7)
    Tree.rotation(Tree.root)
    # right right
    # need left rotation

    # unbalanced