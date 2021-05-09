# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    res = dict()  # 用字典存储对应深度的结果
    def forwardSearch(self, root, depth):
        if root != None:
            if depth not in self.res.keys():
                self.res[depth] = []
            self.res[depth].append(root.val)
            self.forwardSearch(root.left, depth + 1)
            self.forwardSearch(root.right, depth + 1)

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        核心思想：
            类似上一题的方法，先得到层序的结果
            然后将深度为偶数的结果倒序就好了
        """
        self.res = dict()
        self.forwardSearch(root, 1)
        result = []
        for i in self.res.keys():
            if i % 2 == 0:
                result.append(self.res[i][::-1])
            else:
                result.append(self.res[i])
        return result

if __name__ == '__main__':
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    node4 = TreeNode(5)
    root.left = node1
    root.right = node2
    node1.left = node3
    node2.right = node4
    s = Solution()
    print(s.zigzagLevelOrder(root))