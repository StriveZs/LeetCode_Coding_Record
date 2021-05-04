---
title: LeetCode No.98

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第九十八题—验证二叉搜索树
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
```
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
```

## 代码
### 没有AC的版本
虽然没有AC但是我真的没有找到错误！！！！！！！！！！！！因为我写一个一模一样的C++版本就同过了！！！！！
```
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
```

### AC版本
```
class Solution(object):
    pre = -sys.maxsize
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
```