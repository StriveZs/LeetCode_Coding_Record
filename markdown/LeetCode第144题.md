---
title: LeetCode No.143

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第144题—二叉树的前序遍历
最近刚从雁栖湖搬到中关村。各方面和自己的预期很有差异。可能是还是没有适应。  

自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。


![figure.3](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)
 
```
示例 1：

输入：root = [1,null,2,3]
输出：[1,2,3]
示例 2：

输入：root = []
输出：[]

示例 3：

输入：root = [1]
输出：[1]
```
![figure.2](https://assets.leetcode.com/uploads/2020/09/15/inorder_5.jpg)
```
示例 4：
输入：root = [1,2]
输出：[1,2]
```

![figure.1](https://assets.leetcode.com/uploads/2020/09/15/inorder_4.jpg)

```
示例 5：
输入：root = [1,null,2]
输出：[1,2]
 
提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100
```