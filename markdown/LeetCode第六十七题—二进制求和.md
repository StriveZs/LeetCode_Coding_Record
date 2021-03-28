---
title: LeetCode No.67

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第六十七题
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

```
示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
 

提示：

每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。
```

## 代码
15分钟解决，进行二进制加法模拟即可，当然可以偷鸡使用强制类型转换做， 执行用时：36 ms, 在所有 Python3 提交中击败了91.34%的用户内存消耗：14.8 MB, 在所有 Python3 提交中击败了71.90%的用户
```
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str

        核心思想：
                有两种解决办法：
                    1. 直接用Python的强制类型转换 return bin(int(a,2)+int(b,2))[2:]
                    2. 用二进制算法来算 为2进1  模拟进位
                        先补位，将短位数补成长的位数长度
                        在进行进位加法
        """
        result = '' # 结果先用字符串存储
        lenA = len(a)
        lenB = len(b)
        if lenA > lenB:
            str0 = ['0' for i in range(lenA-lenB)]
            t = ''.join(str0)
            b = t + b
            lenB = lenA
        elif lenB > lenA:
            str0 = ['0' for i in range(lenB - lenA)]
            t = ''.join(str0)
            a = t + a
            lenA = lenB
        flag = False # 用来表示短位相加之后是否会进位
        for i in range(lenA):
            tt = 0 # 进位1
            if flag:
                tt = 1
            #print(int(a[lenA-i-1]))
            #print(int(b[lenA-i-1]))
            temp = int(a[lenA-i-1]) + int(b[lenA-i-1]) + tt
            if temp == 3:
                flag = True
                result = '1' + result
            elif temp == 2:
                flag = True
                result = '0' + result
            else:
                flag = False
                result = str(temp) + result
        if flag:
            result = '1' + result
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.addBinary("1", b = "111"))


```