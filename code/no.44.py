class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool

        核心思想：使用动态规划
                构建一个 len(s)+1 * len(p)+1 的dp动态矩阵
                加1是因为：考虑s或p为空的情况下的初始状态
        """
        line = len(p) + 1 # 行
        row = len(s) + 1 # 列
        # 创建dp数组
        dp = [[False]*row for _ in range(line)]
        dp[0][0] = True

        # 单独处理s为空的情况
        if s == "":
            for i in range(len(p)):
                if p[i] != '*':
                    return False
            return True

        # 单独处理p以*开头的情况
        if p.startswith('*'):
            dp[1] = [True]*row

        # 开始处理
        for i in range(1,line):
            isAsterisk = False # 是否为 *
            for j in range(1,row):
                # 处理相等的情况
                if s[j-1] == p[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                # 处理 ? 的情况
                elif p[i-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                # 处理 * 的情况
                elif p[i-1] == '*':
                    # 处理前面已经出现*的情况或者pattern以*开头的情况
                    if dp[i-1][0] == True:
                        dp[i] = [True] * row
                    # 处理顶上为True下一个出现*的情况
                    if dp[i-1][j]:
                        isAsterisk = True
                    # 从该True位置开始后面该行均为True
                    if isAsterisk:
                        dp[i][j] = True

        # 返回结果
        return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    print(s.isMatch(s = "",p = "**a**"))