class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 列举出所有特殊情况：列出特殊情况,而对于其他情况则可以用使用循环处理
        dictList = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']  # 特殊规则字符
        numList = [1,4,5,9,10,40,50,90,100,400,500,900,1000]  # 特殊规则数字

        result = ''

        for i in range(len(dictList)):
            while num >= numList[len(dictList) - i - 1]:  # 要从后往前处理，这样才能保证IV 在 I之前出现
                num -= numList[len(dictList) - i - 1]
                result += dictList[len(dictList) - i - 1]

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(2018))
