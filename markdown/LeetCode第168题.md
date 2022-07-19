---
title: LeetCode No.168

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第168题
## 题目描述
给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。

例如：
```
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
```

示例 1：
```
输入：columnNumber = 1
输出："A"
```
示例 2：
```
输入：columnNumber = 28
输出："AB"
```
示例 3：
```
输入：columnNumber = 701
输出："ZY"
```
示例 4：
```
输入：columnNumber = 2147483647
输出："FXSHRXW"
```

提示：
```
1 <= columnNumber <= 231 - 1
```

## 代码
```
#
# @lc app=leetcode.cn id=168 lang=python
#
# [168] Excel表列名称
#

# @lc code=start
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        思路：这是26进制计算法
        对columnNumber进行取余，余数查表就是结果
        :type columnNumber: int
        :rtype: str
        """
        num2chara = {
            1: 'A',
            2: 'B',
            3: 'C',
            4: 'D',
            5: 'E',
            6: 'F',
            7: 'G',
            8: 'H',
            9: 'I',
            10: 'J',
            11: 'K',
            12: 'L',
            13: 'M',
            14: 'N',
            15: 'O',
            16: 'P',
            17: 'Q',
            18: 'R',
            19: 'S',
            20: 'T',
            21: 'U',
            22: 'V',
            23: 'W',
            24: 'X',
            25: 'Y',
            26: 'Z'
            }
        res = ''
        while columnNumber > 26:
            remainder = columnNumber % 26
            if remainder == 0:
                res = num2chara[26] + res
                columnNumber = (columnNumber - 26) / 26
            else:
                res = num2chara[remainder] + res
                columnNumber = (columnNumber - remainder) / 26
        if columnNumber != 0:
            res = num2chara[columnNumber] + res
        return res

# s = Solution()
# print(s.convertToTitle(columnNumber = 701))

# @lc code=end


```