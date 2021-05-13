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
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        核心思想：
            延续二叉树的层序遍历第一期的思想
            只不过是将最终得到的结果reverse就可以了。
            同样是采用前序遍历，按照深度进行划分，只不过是从最大深度开始存储就可以了
        """
        self.forwardSearch(root, 1)
        result = []
        self.dic = dict()
        for i in self.res.keys():
            result.append(self.res[i])
        return result[::-1]

if __name__ == '__main__':
    root = TreeNode(1)

    s = Solution()
    print(s.levelOrderBottom(root))