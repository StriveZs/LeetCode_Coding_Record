---
title: LeetCode No.50

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第五十题
## 题目描述
现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。

 
```
示例 1：

输入：x = 2.00000, n = 10
输出：1024.00000
示例 2：

输入：x = 2.10000, n = 3
输出：9.26100
示例 3：

输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25
 

提示：

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104
```
## 代码
```
class Solution(object):
    def TimeOut(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float

        核心思想:
                1. 第一种方法，有一个测试用例超时了
                如果n小于0的话，则使用1/x，重复n次
                如果n大于0的话，则使用1*x 重复n次
                如果n等于0的话，返回1
                注意结果要保留5位小数, 结果类型为float

                2. 第二种方法，采用快速幂方法
        """
        if n == 0:
            return 1.0000

        result = float(1.0000)
        flag = True
        if n < 0:
            flag = False
        for i in range(abs(n)):
            if flag:
                result = result * x
            else:
                result = result / x

        return float(format(result,'.5f'))

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float

        核心思想:
                1. 第一种方法，有一个测试用例超时了
                如果n小于0的话，则使用1/x，重复n次
                如果n大于0的话，则使用1*x 重复n次
                如果n等于0的话，返回1
                注意结果要保留5位小数, 结果类型为float

                2. 第二种方法，采用快速幂方法
                快速幂算法能帮我们算出指数非常大的幂，传统的求幂算法之所以时间复杂度非常高（为O(指数n)），
                就是因为当指数n非常大的时候，需要执行的循环操作次数也非常大。
                所以我们快速幂算法的核心思想就是每一步都把指数分成两半，而相应的底数做平方运算。
                这样不仅能把非常大的指数给不断变小，所需要执行的循环次数也变小，而最后表示的结果却一直不会变。

                3^10=3*3*3*3*3*3*3*3*3*3

                //尽量想办法把指数变小来，这里的指数为10

                3^10=(3*3)*(3*3)*(3*3)*(3*3)*(3*3)

                3^10=(3*3)^5

                3^10=9^5
        """
        # 由于python递归和其他语言的递归调用方式不用，因此需要单独声明一个新的函数来进行递归调用
        def call_pow(x,n):
            # 采用递归方式调用
            if n == 0:
                return 1.0
            elif n > 0 and n % 2 == 0:  # 如果指数可以被2取余为0，则x变平方 指数除2  比如: 3^4 变成(3^2)^2 = (3*3)^2
                return call_pow(x * x, n / 2)
            elif n > 0:
                return call_pow(x, n - 1)*x  # 如果n不能被2整除，则减一
            else:
                return 1 / call_pow(x, -n)  # 单独处理n为负数的情况

        return float(format(call_pow(x,n),'.5f'))



if __name__ == '__main__':
    s = Solution()
    print(s.myPow(x = 8.88023, n = 3))
```