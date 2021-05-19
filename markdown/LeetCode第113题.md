---
title: LeetCode No.113

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第113题—路径总和II
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。

![figure.1](https://assets.leetcode.com/uploads/2021/01/18/pathsumii1.jpg)
 
```
示例 1：

输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]
```

![figure.2](https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg)

```
示例 2：

输入：root = [1,2,3], targetSum = 5
输出：[]
示例 3：

输入：root = [1,2], targetSum = 0
输出：[]
 
提示：

树中节点总数在范围 [0, 5000] 内
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
```

## 代码
在上一题的基础上，引入了一个记录路径的数组，这里面不知道为什么
```reasonml
self.sumPath(node.right, curSum + node.val, targetSum, curPath.append(node.val))
```
会报错，因此这里使用了temp列表来最后和curPaht+temp来得到下一层的路径。
```python
python
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    pathList = [] # 路径集合
    def sumPath(self, node, curSum, targetSum, curPath):
        if node == None:
            return
        temp = []
        temp.append(node.val)
        # 如果到达叶子节点，则进行总和判断
        if node.left == None and node.right == None:
            if curSum + node.val == targetSum:
                self.pathList.append(curPath + temp)
        self.sumPath(node.left, curSum + node.val, targetSum,curPath + temp)
        self.sumPath(node.right, curSum + node.val, targetSum, curPath + temp)

    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool

        核心思想：
            采用DFS，每当遇到叶子结点，就去计算当前路径总和，如果等于targetSum, 则将路径添加进去
        """
        self.pathList = []
        self.sumPath(root, 0, targetSum, [])
        return self.pathList

if __name__ == '__main__':
    root = TreeNode(5)
    node1 = TreeNode(4)
    node2 = TreeNode(11)
    node3 = TreeNode(7)
    node4 = TreeNode(2)
    node5 = TreeNode(8)
    node6 = TreeNode(13)
    node7 = TreeNode(4)
    node8 = TreeNode(5)
    node9 = TreeNode(1)
    root.left = node1
    node1.left = node2
    node2.left = node3
    node2.right = node4
    root.right = node5
    node5.left = node6
    node5.right = node7
    node7.left = node8
    node7.right = node9

    s = Solution()
    print(s.pathSum(root,22))

```
