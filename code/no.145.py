# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    res = []
    # fixme: 后序遍历
    def backward(self, node):
        if node is not None:
            self.backward(node.left)
            self.backward(node.right)
            self.res.append(node.val)

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.backward(root)
        return self.res