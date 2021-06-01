---
title: LeetCode No.125

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第125题—验证回文串
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。
```
示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
```
## 代码
执行用时：88 ms, 在所有 Python3 提交中击败了7.76%的用户内存消耗：14.9 MB, 在所有 Python3 提交中击败了96.98%的用户
```python
class Solution(object):
    def judeRange(self, c):
        if c >= 'a' and c <= 'z':
            return True
        elif c >= 'A' and c <= 'Z':
            return True
        elif c >='0' and c <= '9':
            return True
        else:
            return False

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        核心思想:
            双向指针，自动去除出字母和数字之外的字符串
            统一将字母转换为小写
        """
        if len(s) == 0:
            return True
        start = 0
        ends = len(s)-1

        while start < ends:
            flag1 = self.judeRange(s[start])
            flag2 = self.judeRange(s[ends])
            if flag1 and flag2:
                s1 = s[start].lower()
                s2 = s[ends].lower()
                if s1 != s2:
                    return False
                start += 1
                ends -= 1
                continue
            elif flag1 and ~flag2:
                ends -= 1
                continue
            elif ~flag1 and flag2:
                start += 1
                continue
            else:
                start += 1
                ends -= 1
        return True
```
