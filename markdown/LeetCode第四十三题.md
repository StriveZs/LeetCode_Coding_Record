---
title: LeetCode No.43

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第四十三题
## 题目描述
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
```
示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
```

## 代码
本题是经典的大数乘法.  

```
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        核心思想：经典的大数乘法
                核心就是循环 每次分别计算进位和计算余位，注意整数和字符串的转换
        """
        num1_reverse = num1[::-1]
        num2_reverse = num2[::-1]
        result = [str(0) for i in range(1000)]
        for i in range(len(num1_reverse)):
            for j in range(len(num2_reverse)):
                temp = int(num1_reverse[i]) * int(num2_reverse[j])
                # 计算进位
                result[i+j+1] = str(int(result[i+j+1]) + int((int(result[i+j]) + temp) / 10))
                # 计算余位
                result[i+j] = str((int(result[i+j]) + temp) % 10)

        result = result[::-1]
        #print(result)
        str_res = ""
        flag = True
        for i in range(len(result)):
            if flag:
                if result[i] != '0':
                    flag = False
                    str_res += result[i]
            else:
                str_res += result[i]
        # 单独处理为0的情况
        if flag:
            return "0"
        return str_res

if __name__ == '__main__':
    s = Solution()
    print(s.multiply('123','456'))
```