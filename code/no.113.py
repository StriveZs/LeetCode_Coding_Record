# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    pathList = [] # 路径集合
    def sumPath(self, node, curSum, targetSum, curPath):
        if node == None:
            return
        temp = []
        temp.append(node.val)
        # 如果到达叶子节点，则进行总和判断
        if node.left == None and node.right == None:
            if curSum + node.val == targetSum:
                self.pathList.append(curPath + temp)
        self.sumPath(node.left, curSum + node.val, targetSum,curPath + temp)
        self.sumPath(node.right, curSum + node.val, targetSum, curPath + temp)

    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool

        核心思想：
            采用DFS，每当遇到叶子结点，就去计算当前路径总和，如果等于targetSum, 则将路径添加进去
        """
        self.pathList = []
        self.sumPath(root, 0, targetSum, [])
        return self.pathList

if __name__ == '__main__':
    root = TreeNode(5)
    node1 = TreeNode(4)
    node2 = TreeNode(11)
    node3 = TreeNode(7)
    node4 = TreeNode(2)
    node5 = TreeNode(8)
    node6 = TreeNode(13)
    node7 = TreeNode(4)
    node8 = TreeNode(5)
    node9 = TreeNode(1)
    root.left = node1
    node1.left = node2
    node2.left = node3
    node2.right = node4
    root.right = node5
    node5.left = node6
    node5.right = node7
    node7.left = node8
    node7.right = node9

    s = Solution()
    print(s.pathSum(root,22))
