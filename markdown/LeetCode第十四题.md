---
title: LeetCode No.14

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第十四题
## 题目描述
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

 
```
示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
 

提示：

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成
```
## 代码
```
import re

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        if strs[0] == '':
            return ""
        commanForward = ''
        flag = False
        index = -1
        for i in range(len(strs[0])):
            commanForward += strs[0][i]
            j = 1
            while j < len(strs):
                if commanForward != strs[j][0:i+1]:
                    index = i
                    flag = True
                    break
                j += 1
            if flag:
                break
            if ~flag:
                index = i+1
        if index == -1:
            return ""
        else:
            return strs[0][0:index]

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["a","a","b"]))

```