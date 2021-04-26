# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # 中序遍历
    def middle_order(self,node):
        if node != None:
            self.middle_order(node.left)
            self.res.append(node.val)
            self.middle_order(node.right)
    # 先序遍历
    def front_order(self, node):
        if node != None:
            self.res.append(node.val)
            self.front_order(node.left)
            self.front_order(node.right)
    # 后序遍历
    def back_order(self,node):
        if node != None:
            self.back_order(node.left)
            self.back_order(node.right)
            self.res.append(node.val)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        核心思想：
                中序遍历原理：先遍历左子树，在访问根节点，最后遍历右子树
                先序遍历原理：先访问根节点，在遍历左子树，最后遍历右子树
                后序遍历原理：先访问左子树，再遍历右子树，最后访问根节点
        """
        self.res = []
        self.middle_order(root)
        return self.res
