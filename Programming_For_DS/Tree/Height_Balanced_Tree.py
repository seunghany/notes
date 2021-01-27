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
    def __init__(self, root = None):
        self.root = root

    def height(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root):
        if root is None:
            return True

        lh = self.height(root.left)  # left height
        rh = self.height(root.right)  # right height
        if abs(lh-rh) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False

    # step 1 insert
    def insert(self, newNode):
        self.root = self.insertHelp(self.root, newNode)
        if self.isBalanced(self.root):
            print("Balanced")
        else:
            print("Not Balanced")
            # 만약 unBalnced 하다면 rotation이 필요

    def insertHelp(self, curNode, newNode):
        # Base Case
        if not curNode:  # 만약 끝에 도착한다면 새로운 노드 안착
            return TreeNode(newNode)
        if newNode == curNode.val:
            return curNode
        # recursie case
        if curNode.val < newNode:  # 숫자가 작으면 왼쪽으로
            curNode.left = self.insertHelp(curNode.left, newNode)
        else: # 숫자가 크면 오른쪽으로
            curNode.right = self.insertHelp(curNode.right, newNode)

        return curNode




class TreeNode():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == '__main__':
    Tree = HBT()
    Tree.insert(5)
    Tree.insert(6)
    Tree.insert(7)