---
title: LeetCode No.108

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第108题—将有序数组转换为二叉搜索树
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。

高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

![figure.1.1](https://gitee.com/zyp521/upload_image/raw/master/r67QOX.jpg)

![figure.1.2](https://gitee.com/zyp521/upload_image/raw/master/lME5lp.jpg)
```
示例 1：

输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：
```

![figure.2](https://gitee.com/zyp521/upload_image/raw/master/kqM2k2.jpg)

```
示例 2：

输入：nums = [1,3]
输出：[3,1]
解释：[1,3] 和 [3,1] 都是高度平衡二叉搜索树。
 

提示：

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 按 严格递增 顺序排列
```

## 代码
执行用时：32 ms, 在所有 Python 提交中击败了59.87%的用户内存消耗：15.7 MB, 在所有 Python 提交中击败了52.76%的用户  
经典分治思想
```
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
```