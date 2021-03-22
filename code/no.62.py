class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int

        核心思想：
                看到这道题，如果学过动态规划的话，肯定会首先想到使用动态规划来解
                根据题目内容来定义dp[i][j]
                这里的dp[i][j]表示从左上角到达(i,j)位置最多路径数
                动态规划解法:
                    定义 f[i][j] 为到达位置 (i,j) 的不同路径数量。
                    那么 f[n-1][m-1] 就是我们最终的答案，而 f[0][0] = 1 是一个显而易见的起始条件。
                    由于题目限定了我们只能 往下 或者 往右 移动，因此我们按照当前可选方向进行分析：
                        1.当前位置只能往下移动，即有 f[i][j] = f[i-1][j] (边界)
                        2.当前位置只能往右移动，即有 f[i][j] = f[i][j-1] (边界)
                        3.当前位置即能往下也能往右移动，即有 f[i][j] = f[i][j-1] + f[i-1][j]

        """
        dp = [[0 for i in range(n)] for i in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                # 既能往下也能往右移动
                if i > 0 and j > 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1] # 非边界位置，因此它可以是从上边来的，可以是从左边来的
                elif i > 0: # 位于左边界  从上一个点过来只能往下走
                    dp[i][j] = dp[i-1][j]
                elif j > 0: # 位于上边界 从上一个点过来只能往右走
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(m = 3, n = 7))