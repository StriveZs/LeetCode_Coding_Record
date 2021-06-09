# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    sum = 0
    def dfs(self, node, curStr):
        if node != None:
            curStr += str(node.val)
            if node.right == None and node.left == None:
                self.sum += int(curStr)
            self.dfs(node.left, curStr)
            self.dfs(node.right, curStr)

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int

        DFS 强制类型转换并且记录就好了
        """
        self.sum =0
        self.dfs(root, '')
        return self.sum

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    root.left = node1
    root.right = node2
    print(s.sumNumbers(root))