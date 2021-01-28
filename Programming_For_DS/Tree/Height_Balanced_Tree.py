class TreeNode():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        self.bf = 0  # balance factor  -> left.height - right.height

    def printTree(self) -> list:
        result = list()
        thislevel = [self]
        while thislevel:
            nextlevel = list()
            none_list = 1
            for n in thislevel:
                if n != None:
                    none_list = 0
                    break
            if none_list == 1:
                return result

            for n in thislevel:
                if n != None:
                    result.append(n.val)
                    nextlevel.append(n.left)
                    nextlevel.append(n.right)
                else:
                    result.append(None)
                    nextlevel.append(None)
                    nextlevel.append(None)

            thislevel = nextlevel
        return result
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
            # Condition check이 필요함.
            # 일단 traverse the tree using dfs
            # 내 생각엔 postOrder로 하면 될거 같다.
            # 밑에거 부터 찾는게 좋을테니!

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
        if curNode.val > newVal:  # 숫자가 작으면 왼쪽으로
            curNode.left = self.insertHelp(curNode.left, newVal)
        else: # 숫자가 크면 오른쪽으로
            curNode.right = self.insertHelp(curNode.right, newVal)
        # This changes all the balancing factor of ancesctors of newly added Node
        curNode.bf = self.height(curNode.right) - self.height(curNode.left)
        if curNode.bf not in [-1, 0, 1]:  # out of range
            # Out of range
            # Rotation needed
            if curNode.bf == 2:
                # 오른쪽이 unbalnce
                # right right -> left rotation needed
                if curNode.right.bf >= 0:
                    curNode = self.rotateLeft(curNode)
                else:
                    # right left -> right left rotation needed
                    curNode.right = self.rotateRight(curNode.right)
                    # 이제 righttight -> left rotation needed
                    curNode = self.rotateLeft(curNode)
            else:  # curNode.bf == -2
                # 왼쪽이 unbalance
                if curNode.left.bf <= 0:
                    # left left -> right rotation needed
                    curNode = self.rotateRight(curNode)
                else:  # curNode.left.bf  > 0
                    # left right -> left right rotation needed
                    curNode.left = self.rotateLeft(curNode.left)
                    # now left left -> right rotation needed
                    curNode = self.rotateRight(curNode)

        return curNode

    def rotateLeft(self, curNode):
        # left rotation
        newRoot = curNode.right
        oldLeft = newRoot.left  # 여기서 에러남
        newRoot.left = curNode
        curNode.right = oldLeft
        # Remember Curnode's parent have to point at newRoot now.
        # parent.right = rotateRight(self,curNode.right)
        # if curNode is root:
        # self.root = rotateRight(self,curNode.right)
        return newRoot

    def rotateRight(self, curNode):
        # rightRotation
        newRoot = curNode.left
        oldRight = newRoot.right
        newRoot.right = curNode
        curNode.left = oldRight
        # Remember Curnode's parent have to point at newRoot now.
        # parent.left = rotateRight(self,curNode.left)  # if curNode is not root
        return newRoot



if __name__ == '__main__':
    Tree = HBT()

    Tree.insert(5)
    Tree.insert(1)
    Tree.insert(3)
    x = Tree.root.printTree()
    print(x)
    # # print(Tree.root.right.val)
    # Tree.root.right = Tree.rotateRight(Tree.root.right)
    # print("after right rotation")
    # print(Tree.isBalanced(Tree.root))
    # x = Tree.root.printTree()
    # print(x)
    # Tree.root = Tree.rotateLeft(Tree.root)
    # print("after left rotation")
    # print(Tree.isBalanced(Tree.root))
    # x = Tree.root.printTree()
    # print(x)
    # right right
    # need left rotation

    # unbalanced