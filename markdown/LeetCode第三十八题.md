---
title: LeetCode No.38

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第三十八题
## 题目描述
给定一个正整数 n ，输出外观数列的第 n 项。

「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。

你可以将其视作是由递归公式定义的数字字符串序列：

countAndSay(1) = "1"
countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。
前五项如下：
```
1.     1
2.     11
3.     21
4.     1211
5.     111221
第一项是数字 1 
描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"
```
要 描述 一个数字字符串，首先要将字符串分割为 最小 数量的组，每个组都由连续的最多 相同字符 组成。然后对于每个组，先描述字符的数量，然后描述字符，形成一个描述组。要将描述转换为数字字符串，先将每组中的字符数量用数字替换，再将所有描述组连接起来。

例如，数字字符串 "3322251" 的描述如下图：

![figure.1](https://assets.leetcode.com/uploads/2020/10/23/countandsay.jpg)
 
```
示例 1：

输入：n = 1
输出："1"
解释：这是一个基本样例。
示例 2：

输入：n = 4
输出："1211"
解释：
countAndSay(1) = "1"
countAndSay(2) = 读 "1" = 一 个 1 = "11"
countAndSay(3) = 读 "11" = 二 个 1 = "21"
countAndSay(4) = 读 "21" = 一 个 2 + 一 个 1 = "12" + "11" = "1211"
 

提示：

1 <= n <= 30
```

## 代码
```
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        核心思想: 迭代思想，就是从头往后依次找到n相等的那种情况返回（重点是读懂题目）

        """
        if n == 1:
            return str(1)
        s = "1"
        for i in range(n-1):
            t = ""
            i, j = 0, len(s)
            count = 1 # 统计相同个数
            while i < j-1:
                if s[i] == s[i+1]:
                    count += 1
                    i += 1
                else:
                    # 重新统计
                    t = t + str(count) + s[i]
                    count = 1
                    i += 1
            s = t + str(count) + s[i]
        return s

if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(4))

```