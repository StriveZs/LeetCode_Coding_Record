# Definition for a binary tree node.
import sys
import copy
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    errorNode1 = TreeNode() # 记录错误节点1
    errorNode2 = TreeNode() # 记录错误节点2
    pre = TreeNode(-sys.maxsize) # 记录前一个值
    flag = True
    def middleSearch(self,node):
        if node == None:
            return
        self.middleSearch(node.left) # 访问左子树
        if self.pre.val > node.val and self.pre.val != -sys.maxsize: # 这里的-sys.maxsize是一个最小值
            if self.flag:
                self.errorNode1 = self.pre # 由于当前节点小于上一个节点，因此记录上一个节点比如：321 应该是记录3
                self.flag = False
            self.errorNode2 = node # 如321，记录完3之后应该记录1，所以是记录当前node
        self.pre = node
        self.middleSearch(node.right) # 访问右子树

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.

        核心思想：
            依然是采用中序遍历，并记录两个错误顺序的点，最后进行交换
        """
        self.middleSearch(root)
        print(self.errorNode1.val, self.errorNode2.val)
        temp = self.errorNode1.val
        self.errorNode1.val = self.errorNode2.val
        self.errorNode2.val = temp


if __name__ == '__main__':
    root = TreeNode(5)
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(-2147483648)
    node4 = TreeNode(2)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    s = Solution()
    s.recoverTree(root)