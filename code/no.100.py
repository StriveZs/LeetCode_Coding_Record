# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def middle_search(self,node1,node2):
        if node1 == None and node2 == None:
            return True
        elif node1 == None and node2 != None:
            return False
        elif node1 != None and node2 == None:
            return False
        else:
            if self.middle_search(node1.left,node2.left) == False:
                return False
            if node1.val != node2.val:
                return False
            if self.middle_search(node1.right, node2.right) == False:
                return False
            return True
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        
        核心思想：
                同时对两个棵树进行先序遍历、中序遍历、后序遍历都可以，执行DFS就行了，然后同时比较结果，
            如果存在不同的情况，则返回False
        """
        return self.middle_search(p,q)