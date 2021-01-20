---
title: LeetCode No.13

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第十三题
## 题目描述
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
```
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

```
示例 1:

输入: "III"
输出: 3
示例 2:

输入: "IV"
输出: 4
示例 3:

输入: "IX"
输出: 9
示例 4:

输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.
示例 5:

输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
 
```
提示：

题目所给测试用例皆符合罗马数字书写规则，不会出现跨位等情况。
IC 和 IM 这样的例子并不符合题目要求，49 应该写作 XLIX，999 应该写作 CMXCIX 。
关于罗马数字的详尽书写规则，可以参考 罗马数字 - Mathematics 。

## 代码
```
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictList = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']  # 特殊规则字符
        numList = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]  # 特殊规则数字

        dicts = zip(dictList,numList)
        dicts = dict(dicts)
        dictSet = set(dictList)
        result = 0
        i = len(s) - 1
        while i >= 0:
            if i == 0:
                result += dicts[s[i]]
                i -= 1
            else:
                if s[i] == 'V' or s[i] == 'X':
                    if s[i - 1] == 'I':
                        temp = s[i - 1] + s[i]
                        result += dicts[temp]
                        i -= 2
                    else:
                        result += dicts[s[i]]
                        i -= 1
                elif s[i] == 'L' or s[i] == 'C':
                    if s[i - 1] == 'X':
                        temp = s[i - 1] + s[i]
                        result += dicts[temp]
                        i -= 2
                    else:
                        result += dicts[s[i]]
                        i -= 1
                elif s[i] == 'D' or s[i] == 'M':
                    if s[i - 1] == 'C':
                        temp = s[i - 1] + s[i]
                        result += dicts[temp]
                        i -= 2
                    else:
                        result += dicts[s[i]]
                        i -= 1
                else:
                    result += dicts[s[i]]
                    i -= 1
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('CX'))
```