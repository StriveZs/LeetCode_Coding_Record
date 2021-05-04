# Definition for a binary tree node.
import sys
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    valList = []
    pre = -sys.maxsize
    def middleSearch(self, node):
        if node == None:
            return
        self.middleSearch(node.left)
        self.valList.append(node.val)
        self.middleSearch(node.right)
        return

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        题目分析：
            二叉搜索树具有如下特征：
                节点的左子树只包含小于当前节点的数。
                节点的右子树只包含大于当前节点的数。
                所有左子树和右子树自身必须也是二叉搜索树

            采用中序遍历，如果遍历当前的数值比上一次遍历的结果小则返回false，证明不是二叉搜索树
        """
        if root.left == None and root.right == None:
            return True
        self.middleSearch(root)
        for i in range(1,len(self.valList)):
            if self.valList[i] <= self.valList[i-1]:
                return False
        return True
    def new(self,node):
        if node != None:
            if self.new(node.left) == False:
                return False
            if node.val <= self.pre:
                return False
            self.pre = node.val
            return self.new(node.right)
        else:
            return True

    def newVersion(self,root):
        if root.left == None and root.right == None:
            return True
        return self.new(root)

if __name__ == '__main__':
    root = TreeNode(0)
    node1 = TreeNode(1)
    root.right = node1
    s = Solution()
    print(s.newVersion(root))