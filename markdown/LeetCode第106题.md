---
title: LeetCode No.106

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第106题—从中序与后序遍历序列构造二叉树
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。
```
例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
```

## 代码
我只改了我105题一行代码。其实就是把后序遍历的节点从队尾读取，而对于前序遍历的话则是从队首读取就可以了
```
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
```