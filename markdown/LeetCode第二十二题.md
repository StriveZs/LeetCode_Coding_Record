---
title: LeetCode No.22

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第二十二题
## 题目描述
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 
```
示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]
 

提示：

1 <= n <= 8
```

## 代码
```
class Solution(object):
    def func(self,strlist, string, l, r, n):
        # 单边递归结束条件
        if l > n or r > n or r > l:
            return

        # string生成结束条件
        if l == n and r == n:
            strlist.append(string)
            return
        self.func(strlist, string + '(', l+1, r, n)
        self.func(strlist, string + ')', l, r+1, n)
        return


    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        strlist = []
        self.func(strlist, "", 0, 0, n)
        return strlist

if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))

```