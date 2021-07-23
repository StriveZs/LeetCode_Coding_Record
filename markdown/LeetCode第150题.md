---
title: LeetCode No.150

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第150题—逆波兰表达式求值

自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
根据 逆波兰表示法，求表达式的值。

有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

 

说明：
- 整数除法只保留整数部分。
- 给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
 
```
示例 1：

输入：tokens = ["2","1","+","3","*"]
输出：9
解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
示例 2：

输入：tokens = ["4","13","5","/","+"]
输出：6
解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6
示例 3：

输入：tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
输出：22
解释：
该算式转化为常见的中缀算术表达式为：
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

提示：

1 <= tokens.length <= 104
tokens[i] 要么是一个算符（"+"、"-"、"*" 或 "/"），要么是一个在范围 [-200, 200] 内的整数
```
## 代码
可以说只要想到用栈和理解逆波兰式的含义就十分简单了。唯一一点就是要注意只取整数部分，不考虑小数部分。
```
import math
class Solution(object):
    def evalRPN(self, tokens):
        """
        逆波兰式是后缀表达式
        后缀表达式的求法：只需要处理符号的前两个值就可以了
        那么就可以考虑使用栈来模拟计算过程
        需要注意的是，这里只取整数部分，不考虑小数 因此考虑使用math.modf()
        :type tokens: List[str]
        :rtype: int
        """
        stack = [] # 数字栈
        characters = ['-', '+', '*', '/'] # 符号
        for i in range(len(tokens)):
            if tokens[i] in characters:
                b = stack[-1]
                stack.pop()
                a = stack[-1]
                stack.pop()
                if tokens[i] == '-':
                    c = a - b
                elif tokens[i] == '+':
                    c = a + b
                elif tokens[i] == '*':
                    c = a * b
                elif tokens[i] == '/':
                    c = a / b
                stack.append(math.modf(c)[1])
            else:
                stack.append(int(tokens[i]))
        return int(stack[-1])

if __name__ == '__main__':
    s = Solution()
    print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
```