---
title: LeetCode No.166

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第166题—分数到小数
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

好久没更新了 忙于科研来着 害 都是为了毕业。最近又把自己的事情捡起来了。

## 题目描述
给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。

如果小数部分为循环小数，则将循环的部分括在括号内。

如果存在多个答案，只需返回 任意一个 。

对于所有给定的输入，保证 答案字符串的长度小于 104 。

 
```
示例 1：

输入：numerator = 1, denominator = 2
输出："0.5"
示例 2：

输入：numerator = 2, denominator = 1
输出："2"
示例 3：

输入：numerator = 2, denominator = 3
输出："0.(6)"
示例 4：

输入：numerator = 4, denominator = 333
输出："0.(012)"
示例 5：

输入：numerator = 1, denominator = 5
输出："0.2"
```

提示：
```
-231 <= numerator, denominator <= 231 - 1
denominator != 0
```

## 代码
思路: 就是模拟大数除法的过程，结合上队列来实现重复被除数查询，从而实现括号的添加。特别注意负数和整除的情况

代码如下:(其中第一个想法是只针对比较单一的情况)

```
#
# @lc app=leetcode.cn id=166 lang=python
#
# [166] 分数到小数
#

# @lc code=start
import re
import math

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        除法运算, 实质为:寻找重复位数
        分两种情况来进行判断:
            1. 直接整除的情况，直接转换为小数就可以了
            2. 不能整除，小数部分为循环小数的情况。
        整体做法均为要用代码实现出发运算过程，包括借位等操作
        针对循环小数的情况：
            1. 最简单的就是2/3 4/3等这种单位循环的小数 0.(6) 1.(6)等等 这种通过下面Version1的代码就可以实现（只需要判断当前被除数和上个被除数是否相同即可了）
            但是这个不适用于4/333的情况，因为它是多位小数循环的情况，单凭上面的思路无法实现
            2. 因此我考虑了新的方法，建立一个队列存储生成的被除数，只要在点了小数点之后就是将所有的被除数存储，然后累积存储被除数直到重复，则将对应重复被除数之间的所有小数点位数用括号括起来
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # 判断是否能够整除
        if numerator % denominator == 0:
            return str(numerator / denominator)
        # 思路一
        ## 模拟除法运算
        '''
        res = '' # 保存结果
        flag = True # 标志着重复 被除数连着两次重复
        flag1 = False # 标志小数点使用了
        pre_div = numerator # 存储上一个被除数 当上一个被除数和当前被除数
        trade = 0 # 商
        while flag:
            trade = int(numerator / denominator)
            if trade == 0:
                if res == '': # 单独处理2/3商为0的情况
                    res = '0'
                    res += '.'
                    flag1 = True
                else:
                    #res += str(trade)
                    if '.' not in res:
                        res += '.'
                        flag1 = True
                pre_div = numerator
                numerator = numerator * 10 - trade * denominator
            else:
                res += str(trade)
                pre_div = numerator
                numerator = numerator - trade * denominator
                if flag1:
                    numerator = numerator * 10
            if pre_div == numerator:
                res = res[:-1] + '(' + res[-1] + ')'
                break
            if numerator == 0:
                break
        return res
        '''

        # 思路二
        ## 模拟除法运算+被除数队列记忆
        # 负数处理
        flag2 = False # 负数标志
        if numerator < 0 and denominator < 0:
            numerator = abs(numerator)
            denominator = abs(denominator)
        elif numerator < 0:
            numerator = abs(numerator)
            flag2 = True
        elif denominator < 0:
            denominator = abs(denominator)
            flag2 = True
        res = '' # 结果保存
        flag = True # 标志是否结束
        flag1 = False # 标志小数点使用了
        numerator_list = [] # 存储被除数的list
        trade = 0 # 商
        while flag:
            trade = int(numerator / denominator)
            if trade == 0:
                if res == '': # 单独处理2/3商为0的情况
                    res = '0'
                    res += '.'
                    flag1 = True
                    numerator = numerator * 10
                else:
                    #res += str(trade)
                    if '.' not in res:
                        res += '.'
                        flag1 = True
                        numerator = numerator * 10
                    else:
                        res += '0'
                        numerator_list.append(numerator)
                        numerator = numerator * 10 - trade * denominator
            else:
                res += str(trade)
                if '.' in res:
                    numerator_list.append(numerator)
                numerator = numerator - trade * denominator
                if flag1:
                    numerator = numerator * 10
            # 如果numerator在numerator_list中，则证明重复了
            if numerator in numerator_list:
                # 分两种情况，第一种是单位重复，第二种是多位重复
                # 单位重复
                if numerator == numerator_list[-1]:
                    res = res[:-1] + '(' + res[-1] + ')'
                    break
                # 多位重复
                else:
                    index = numerator_list.index(numerator) # 找到重复被除数的下标
                    point_index = res.index('.') # 找到小数点的位数
                    offset = 2 # 偏移量
                    if len(res[:point_index]) != 1:
                        offset = point_index + 1
                    res = res[: index+offset] + '(' + res[index+offset:] + ')'
                    break
            if numerator == 0:
                break
        if flag2:
            res = '-' + res
        return res


s = Solution()
print(s.fractionToDecimal(numerator = 420, denominator = 226))
        


# @lc code=end


```