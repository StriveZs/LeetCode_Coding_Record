---
title: LeetCode No.105

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第105题—从前序与中序遍历序列构造二叉树
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

```
例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
```

## 代码
```
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def irritationBuildTree(self,preorder,inorder):
        if len(preorder) == 0: # 则证明没有根节点了
            return None
        curRoot = preorder.pop(0) # 获得当前子树根节点
        node = TreeNode(curRoot) # 生成节点
        index = inorder.index(curRoot) # 获得当前根节点在中序遍历中的位置，左边划分为左子树，右边为右子树
        node.left = self.irritationBuildTree(preorder[:index],inorder[:index]) # 递归构建左子树
        node.right = self.irritationBuildTree(preorder[index:],inorder[index+1:]) # 递归构建右子树
        return node

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode

        核心思想：
            根据前序遍历和中序遍历来确定一颗二叉树
            1.确定树的根节点,树根是当前树中所有元素在前序遍历中最先出现的元素。

            2.求解树的子树,找出根节点在中序遍历中的位置，根左边的所有元素就是左子树，
            根右边的所有元素就是右子树。若根节点左边或右边为空，则该方向子树为空；
            若根节点左边和右边都为空，则根节点已经为叶子节点。

            3.递归求解树,将左子树和右子树分别看成一棵二叉树，重复1、2、3步，直到所有的节点完成定位。
        """
        return self.irritationBuildTree(preorder,inorder)

if __name__ == '__main__':
    s = Solution()
    print(s.irritationBuildTree([3,9,20,15,7],[9,3,15,20,7]))
```
