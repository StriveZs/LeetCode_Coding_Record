---
title: LeetCode No.95

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第九十五题—不同的二叉搜索II
## 题目描述
给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。

```

示例：

输入：3
输出：
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释：
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
 

提示：

0 <= n <= 8
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
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]

        题目分析：
                根据给的例子可以看出，每个访问的情况都是使用的中序遍历，而且中序遍历得到的结果要满足[1,2,3]
                二叉搜索树的性质：
                    根节点的左子树的元素都要小于根节点，根节点的右子树元素都要大于根节点
                根据上面性质可以想到，对于每一个子树都满足上述的性质，因此可以将问题看成一个分而治之的问题，

        解题思路：
                采用分治的方法，选取一个节点作为根节点，前面的部分作为作为左子树，后面的部分作为右子树
                针对左子树，同样采样上述方法，针对右子树同样采用上述方法
                依次按照上述方法划分，然后在进行拼接即可
        """
        if n == 0:
            return []
        def generateSearchTree(start,end):
            if start > end:
                return [None,]
            allTress = []
            for i in range(start,end+1): # 针对所有情况进行枚举，因为每个节点都可以作为根节点
                # 对左子树建立二叉搜索树
                leftTree = generateSearchTree(start,i-1) # 获得所有的左子树的可能

                # 针对右子树建立二叉搜索树
                rightTree = generateSearchTree(i+1,end) # 所有所有右子树的可能

                # 针对对左子树和右子树进行组合，将他们分别拼接到根节点上
                for lt in leftTree:
                    for rt in rightTree:
                        current_root = TreeNode(i) # 当前根节点
                        current_root.left = lt # 拼接左子树
                        current_root.right = rt # 拼接右子树
                        allTress.append(current_root) # 添加到当前根节点对应的划分情况
            # 针对子级调用的话，则上一次就返回的是以这个根节点为划分的左子树/右子树的所有可能
            # 如上面rightTree/leftTree 进行generateSearchTree调用返回的是这个子树对应的所有二叉搜索树的情况
            # 对于最开始的调用，则返回的就是最终的结果
            return allTress
        return generateSearchTree(1,n)
```