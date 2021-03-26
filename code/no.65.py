class Solution(object):
    # 确定当前字符串对应的状态
    def make(self,c):
        if c == ' ':
            return 0
        elif c == '+':
            return 1
        elif c == '-':
            return 1
        elif c == '.':
            return 3
        elif c == 'e' or c == 'E':
            return 4
        else:
            # 数字情况
            if c >= '0' and c <= '9':
                return 2
            # 其他情况
            else:
                return 5
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool

        核心思想：
                使用DFA求解
                分析题意、画出状态转移图(可以不是最简的)
                根据状态转移图写出状态转移表
                状态共8个状态，下标为0、1、2、3、4、5、6、7、8、9
                所有状态：
                    0. 初始状态
                    1.符号位
                    2.整数部分
                    3.左侧有整数的小数点
                    4.左侧无整数的小数点（根据前面的第二条额外规则，需要对左侧有无整数的两种小数点做区分）
                    5.小数部分
                    6.字符 e/E
                    7.指数部分的符号位
                    8.指数部分的整数部分
        """
        state = 0 # 当前状态
        finals = [0,0,0,1,0,1,1,0,1]  # 最终可接受的状态 1表示可以介绍 0表示不可以接收
        # 状态转移表
        transfer = [[ 0, 1, 6, 2,-1,-1],
                    [-1,-1, 6, 2,-1,-1],
                    [-1,-1, 3,-1,-1,-1],
                    [ 8,-1, 3,-1, 4,-1],
                    [-1, 7, 5,-1,-1,-1],
                    [ 8,-1, 5,-1,-1,-1],
                    [ 8,-1, 6, 3, 4,-1],
                    [-1,-1, 5,-1,-1,-1],
                    [ 8,-1,-1,-1,-1,-1]]

        for i in range(len(s)):
            state = transfer[state][self.make(s[i])] # 访问状态转移表，确定下一个转移到的状态
            if state < 0: # 状态达到不可接受状态
                return False

        return bool(finals[state])

if __name__ == '__main__':
    s = Solution()
    print(s.isNumber('95a54e53'))
