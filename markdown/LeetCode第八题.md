---
title: LeetCode No.8

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第八题
又是辛勤劳动的一天呢QWQ。  

## 题目描述
请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：

如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0 。

注意：

本题中的空白字符只包括空格字符 ' ' 。
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  231 − 1 或 −231 。
 
```
示例 1:

输入: "42"
输出: 42
示例 2:

输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
示例 3:

输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
示例 4:

输入: "words and 987"
输出: 0
解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
     因此无法执行有效的转换。
示例 5:

输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。 
     因此返回 INT_MIN (−231) 。
 

提示：

0 <= s.length <= 200
s 由英文字母（大写和小写）、数字、' '、'+'、'-' 和 '.' 组成
```

## 代码
```
class Solution(object):
    # 判断是否为数字
    def isNum(self,s):
        if s == '0' or s == '1' or s == '2' or s == '3' or s == '4' or s == '5' or \
        s == '6' or s == '7' or s == '8' or s == '9':
            return True
        else:
            return False

    # 丢弃开头空白字符
    def deleteKong(self,s):
        index = 0
        for i in range(len(s)):
            if s[i] != ' ':
                index = i
                break
        s = s[index:]
        return s

    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = self.deleteKong(s)
        flag = False # 正负标志
        if len(s) == 0:
            return 0
        if len(s) == 1 and s[0] == '-':
            return 0
        if len(s) == 1 and s[0] == '+':
            return 0
        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                flag = True
            else:
                flag = False
            s = s[1:]
        if self.isNum(s[0]):
            result = ''
            for i in range(len(s)):
                if self.isNum(s[i]):
                    result += s[i]
                else:
                    break
            result = int(result)
            if result < -(2**31) or result > (2**31)-1:
                if flag:
                    return -(2**31)
                else:
                    return (2**31)-1
            else:
                if flag:
                    return -1*result
                else:
                    return result
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi('2147483648'))
```