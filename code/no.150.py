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