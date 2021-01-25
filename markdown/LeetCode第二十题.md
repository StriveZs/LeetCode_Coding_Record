---
title: LeetCode No.20

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第二十题
## 题目描述
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

```
示例 1：

输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：

输入：s = "(]"
输出：false
示例 4：

输入：s = "([)]"
输出：false
示例 5：

输入：s = "{[]}"
输出：true
 

提示：

1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成
```

## 代码
```
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        string = list(s)
        stack = []
        flag = True
        for s in string:
            if s == '(' or s == '[' or s == '{':
                stack.append(s)
            elif s == ')':
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if temp != '(':
                    return False
            elif s == ']':
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if temp != '[':
                    return False
            elif s == '}':
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if temp != '{':
                    return False
        if len(stack) != 0:
            return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isValid("{{{{"))



```