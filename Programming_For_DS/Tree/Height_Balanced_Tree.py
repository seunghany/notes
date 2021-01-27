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

    # step 1 insert
    def insert(self, newNode):
        if type(newNode) == int:
            newNode = TreeNode(newNode)
        self.root = self.insertHelp(self.root, newNode)

    def insertHelp(self, curNode, newNode):
        # if Tree is empty, the new node becomes the root
        if self.root is None:
            self.root = newNode

        if not curNode:  # 만약 끝에 도착한다면 새로운 노드 안착
            return newNode

        if curNode.val < newNode.val:  # 숫자가 작으면 왼쪽으로
            curNode.left = self.insertHelp(curNode.left, newNode)
        else: # 숫자가 크면 오른쪽으로
            curNode.right = self.insertHelp(curNode.right, newNode)




class TreeNode():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == '__main__':
    Tree = HBT()
    Tree.insert(5)
    Tree.insert(6)