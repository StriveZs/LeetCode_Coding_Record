---
title: LeetCode No.69

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第六十九题—x的平方根
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
```
示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去
```

## 原理
牛顿法（数值分析中使用到的）:
在迭代过程中，以直线代替曲线，用一阶泰勒展式（即在当前点的切线）代替原曲线，求直线与 xx 轴的交点，重复这个过程直到收敛。
首先随便猜一个近似值 xx，然后不断令x等于x和a/x的平均数，迭代个六七次后 xx 的值就已经相当精确了

构造方程`$ x - a^{2} = 0 $`，令`$ f(x)=x-a^{2} $`,然后不断用(x,f(x))的切线来不断逼近方程`$ x^{2} $`
上述函数导数为2x，也就是说函数上任意一点(x,f(x))处的切线斜率为2x。
那么x-f(x)/(2x)就是一个比x更接近的近似值，代入`$ f(x)=x^{2}-a $`可以得到`$ x-(x^{2}-a)/(2x) $`
变形即可得到(x+a/x)/2 这里的a是目标值

## 代码
```
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int

        核心思想：
                1. 直接return int(sqrt(x)) 直接ac
                2. 使用暴力遍历方法 for i in range(1,x) 尝试 i*i 是否 == x 或者 i*i < x 但是 (i+1)(i+1) > x
                3. 使用牛顿法（数值分析中使用到的）:
                    在迭代过程中，以直线代替曲线，用一阶泰勒展式（即在当前点的切线）代替原曲线，求直线与 xx 轴的交点，重复这个过程直到收敛。
                    首先随便猜一个近似值 xx，然后不断令x等于x和a/x的平均数，迭代个六七次后 xx 的值就已经相当精确了

                    构造方程x - a^{2} = 0，令f(x)=x-a^{2},然后不断用(x,f(x))的切线来不断逼近方程x^{2}
                    上述函数导数为2x，也就是说函数上任意一点(x,f(x))处的切线斜率为2x。
                    那么x-f(x)/(2x)就是一个比x更接近的近似值，代入f(x)=x^{2}-a可以得到x-(x^{2}-a)/(2x)
                    变形即可得到(x+a/x)/2 这里的a是目标值
        """
        if x == 0:
            return 0
        cur_x = x # 令初始值为x
        while cur_x-x/cur_x > 1e-6:
            cur_x = (cur_x + x/cur_x)/2 # 利用公式(x+a/x)/2计算得到新的a
        return int(cur_x)

if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(8))
```