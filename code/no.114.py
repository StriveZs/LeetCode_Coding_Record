# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        self.flatten(root.left)
        self.flatten(root.right)

        right = root.right
        # 将左子树替换掉右子树
        root.right = root.left
        root.left = None

        # 找到右子树最右的节点，接上原右子树
        p = root
        while (p.right != None):
            p = p.right
        p.right = right