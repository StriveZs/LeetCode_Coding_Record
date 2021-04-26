---
title: LeetCode No.94

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第九十四题—二叉树的中序遍历
## 题目描述
给定一个二叉树的根节点 root ，返回它的 中序 遍历。

![figure.1](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)

```
示例 1：

输入：root = [1,null,2,3]
输出：[1,3,2]
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
输出：[2,1]
```

![figure.3](https://assets.leetcode.com/uploads/2020/09/15/inorder_4.jpg)

```
示例 5：

输入：root = [1,null,2]
输出：[1,2]
 
提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100
```

## 代码
```
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        核心思想：
                中序遍历原理：先遍历左子树，在访问根节点，最后遍历右子树
        """
        self.res = []
        def middle_order(node):
            if node != None:
                middle_order(node.left)
                self.res.append(node.val)
                middle_order(node.right)
        
        middle_order(root)
        return self.res
```