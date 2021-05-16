# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def depth(self, node):
        if node == None:
            return 0
        leftDepth = self.depth(node.left)
        rightDepth = self.depth(node.right)
        return max(leftDepth,rightDepth)+1 # 自底下上深度依次增加

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        核心思想：
            平衡二叉树是一棵每个节点的左右子树的高度差绝对值不超过1的树
            判断方法的话，采用递归+深度的方法
            这里还是考虑自底向上的方法
            每往上一层的深度就增加1
            采用先序遍历方法来遍历的话，这样就先确定左子树的深度，再确定右子树的深度

            同样考虑使用分治的方法
        """
        if root == None:
            return True
        if abs(self.depth(root.left) - self.depth(root.right)) > 1:
            return False
        # 分治处理每个子树
        ## 处理左子树
        if not self.isBalanced(root.left):
            return False
        ## 处理右子树
        if not self.isBalanced(root.right):
            return False
        return True

if __name__ == '__main__':
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(3)
    node5 = TreeNode(4)
    node6 = TreeNode(4)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node3.left = node5
    node3.right = node6
    s = Solution()
    print(s.isBalanced(root))
