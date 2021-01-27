# Level Order (Breadth-First) Traversal

# Visit nodes from left to right, and from top to bottom
class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree():
    def __init__(self, root = None):
        self.root = root

    def visit(self, node: TreeNode):
        print(node.val)


    def BFT(self):
        '''
        Breadth = 폭
        Level Order (Breadth-First) Traversal
        Visit nodes from left to right, and from top to bottom

        '''
        if self.root == None:
            return
        q = [self.root]
        # 이거 list 대신 Double-Linked-List 가 더 빠름
        # from collections import deque
        #   - append(X), appendleft(x),
        #   - pop(), popleft()
        while q:
            curNode = q.pop(0)
            self.visit(curNode)

            for childNode in curNode.child:
                if childNode:
                    q.append(childNode)

    def DFT_preorder(self):
        '''
        Depth = 깊이
        Depth First Traversals

        3 Types
            - PreOrder
            - InOrder
        '''
        self.__DFT__preorderHelp(self):

    def __DFT__