---
title: LeetCode No.2

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第2题
## 题目描述
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例1：

![figure.1](https://gitee.com/zyp521/upload_image/raw/master/ba4SnQ.jpg)

```
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]

```

## 代码
代码这里使用的list格式，对于题目要求的格式只需要进行二者的格式转换就可以了
```
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: List
        :type l2: List
        :rtype: List
        """
        
        l1 = [l1[len(l1)-i-1] for i in range(len(l1))]
        str1 = ""
        for i in range(len(l1)):
            str1 = str1 + str(l1[i])
        # print(int(str1))
        l2 = [l2[len(l2) - i - 1] for i in range(len(l2))]
        str2 = ""
        for i in range(len(l2)):
            str2 = str2 + str(l2[i])
        # print(int(str1))
        result = list(str(int(str1) + int(str2)))
        result_list = []
        #print(result)
        for i in range(len(result)):
            result_list.append(int(result[len(result) - i - 1]))
        #print(result_list)
        return result_list


if __name__ == '__main__':
    s = Solution()
    s.addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9])
```