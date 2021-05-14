# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def balancedBST(self,partNode):
        if len(partNode) == 1:
            return TreeNode(partNode[0])
        middle = int(len(partNode)/2)
        node = TreeNode(partNode[middle])
        node.left = self.balancedBST(partNode[0:middle])
        if middle == len(partNode)-1:
            node.right = None
        else:
            node.right = self.balancedBST(partNode[middle+1:])
        return node
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode

        核心思想：
            高度平衡的二叉树：每个节点的左右子树的高度差绝对值不超过1
            而且有要求是二叉搜索树，因此中序遍历要是升序

            综合上述条件，我们需要将中间的节点作为根节点，这样就划分成一个分而治之的问题了
            分治思想：每个划分的部分都是以中间节点作为当前子树的根节点
        """
        return self.balancedBST(nums)