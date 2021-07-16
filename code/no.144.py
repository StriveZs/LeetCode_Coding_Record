# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    res = []
    # fixme: 前序遍历
    def forward(self, node):
        if node is not None:
            self.res.append(node.val)
            self.forward(node.left)
            self.forward(node.right)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.forward(root)
        return self.res


