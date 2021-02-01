---
title: LeetCode No.29

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第二十九题
## 题目描述
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

 
```
示例 1:

输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2
 

提示：

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
```
## 代码
```
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        i, a, b = 0, abs(dividend), abs(divisor)
        # 被除数小于除数的情况直接返回0
        if a == 0 or a < b:
            return 0

        while b <= a:
            b = b << 1  # 位运算 位左移1位
            i = i + 1  # i为2幂
        else:
            res = (1 << (i - 1)) + self.divide(a - (b >> 1), abs(divisor)) # 用减法来得到商
            if (dividend ^ divisor) < 0: # 负结果判断
                res = -res
            return min(res, (1 << 31) - 1) # 去掉溢出情况

```