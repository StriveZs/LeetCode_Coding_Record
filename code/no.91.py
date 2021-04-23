class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int

        核心思想：动态规划
                s[i]只包含数字，其可能为0

                第一步：定义dp数组
                    dp[i]表示前i个数字解码的个数，结果直接返回dp[-1]
                第二步：确定状态转移方程
                    状态转移方程表示了大规模的问题如何由小规模问题转换而来
                    即如何用dp[i-1]...dp[0]来得到dp[i]

                    本题分析：对于两个字符来说，只存在被解码成0种、1种、2种的情况，所以需要分别讨论上述情况是如何得到的
                    具体讨论如下:
                        ① s[i]不在合法集合中即s[i]为0，这是来考察si[i-1]+s[i]=[i-1:i+1]的
                            - 对于0s[i]这种情况，必然不在合法集合中，直接返回0
                            - 但是对于s[i]0这种情况，是存在合法情况的，如10 20
                        ② s[i]在合法集合中，考察si[i-1]+s[i]=[i-1:i+1]的
                            - s[i-1:i+1]不在合法集合中，即大于26或者小于1的情况，无法解码
                            - s[i-1:i+1]在合法集合中，即在1-26之间，但是需要注意这种情况是可以进行拆分解码的
                            拆分之后会影响后面的解码情况的
        """
        if s[0] == '0':
            return 0
        length = len(s)
        if length == 1:
            return 1
        # 生成数组
        legal = set(str(i) for i in range(1,27))
        dp = [0] * length # 初始化dp数组
        dp[0] = 1 # 设置s[0]对应的解码为1
        if s[1] not in legal:  # s[1]为0
            dp[1] = 1 if s[: 2] in legal else 0
        else:
            dp[1] = 2 if s[: 2] in legal else 1
        for i in range(2,length):
            # 处理剩下的情况  13023
            ## 合法情况
            if s[i] in legal:
                if s[i-1:i+1] in legal:
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
            else:
                if s[i-1:i+1] in legal:
                    dp[i] = dp[i-2]
                else:
                    return 0
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings("12"))