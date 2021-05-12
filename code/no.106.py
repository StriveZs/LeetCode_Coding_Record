# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def irritationBuildTree(self,postorder,inorder):
        if len(postorder) == 0: # 则证明没有根节点了
            return None
        curRoot = postorder.pop() # 获得当前子树根节点
        node = TreeNode(curRoot) # 生成节点
        index = inorder.index(curRoot) # 获得当前根节点在中序遍历中的位置，左边划分为左子树，右边为右子树
        node.left = self.irritationBuildTree(postorder[:index],inorder[:index]) # 递归构建左子树
        node.right = self.irritationBuildTree(postorder[index:],inorder[index+1:]) # 递归构建右子树
        return node
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode

        核心思想：
            类似上一道题，只不过从前序遍历变成了后序遍历
            后序遍历的话，最后的元素为当前子树的根节点，其他的同理
        """
        return self.irritationBuildTree(postorder, inorder)