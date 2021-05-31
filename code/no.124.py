import sys
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    max_sum = -sys.maxsize
    def dfs_statistic_path(self, root):
        if root == None:
            return 0
        left_sum = max(0, self.dfs_statistic_path(root.left)) # 统计左子树的路径总和
        right_sum = max(0, self.dfs_statistic_path(root.right)) # 统计右子树的路径总和
        temp = left_sum + root.val + right_sum # 统计当前路径总和
        self.max_sum = max(self.max_sum, temp) # 和当前最大路径进行比较
        return max(left_sum,right_sum) + root.val # 由于不能够返回(节点不能够重复)，因此只能选择出最大的一个子树再加上当前根节点值来返回

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        整体上是分而治之的思想，看成一个个子问题
        将每个节点看成是它子树的路径和(左子树和右子树)+他本来的值
        只有子路径和大于0的时候才会去统计它
        """
        self.dfs_statistic_path(root)
        return self.max_sum

if __name__ == '__main__':
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    root.left = node1
    root.right = node2
    s = Solution()
    print(s.maxPathSum(root))