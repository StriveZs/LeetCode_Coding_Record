class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int

        核心思想：
                看到这道题，如果学过动态规划的话，肯定会首先想到使用动态规划来解
                根据题目内容来定义dp[i][j]
                这里的dp[i][j]表示从左上角到达(i,j)位置最多路径数
                动态规划解法:
                    定义 f[i][j] 为到达位置 (i,j) 的不同路径数量。
                    那么 f[n-1][m-1] 就是我们最终的答案，而 f[0][0] = 1 是一个显而易见的起始条件。
                    由于题目限定了我们只能往下或者往右移动，同时又存在障碍物
                    因此我们的行动分析如下：
                    1.当前obstacleGrid[i][j]不是障碍物的情况
                        1.1.当前位置只能往下移动，即有 f[i][j] = f[i-1][j] (边界)
                        1.2.当前位置只能往右移动，即有 f[i][j] = f[i][j-1] (边界)
                        1.3.当前位置即能往下也能往右移动，即有 f[i][j] = f[i][j-1] + f[i-1][j]
                    2.当前obstacleGrid[i][j]是障碍物的情况
                        2.1 将dp[i][j]设置为0

                    对于不是障碍物情况的分析：当前位置不是障碍物，那么即时它是从障碍物过来的点也无所谓
                    因为我们已经将障碍物对应的dp值设为了0，对于可能1的3三种情况分析：
                    1.1 从上边过来的，但是上面那个位置是障碍物，因为我们将障碍物对应的dp设为1了，因此当前点即时不是障碍物
                        但是由于它只能从障碍物过来，因此它的dp值等于障碍物的dp值为0
                    1.2 同理只能从左边过来的，由于左边是障碍物，因此它的dp值也等于障碍物的dp值为0
                    1.3 既能从左也能从上过来的，如果左边是障碍物那么当前dp=障碍物dp+从上过来的dp=从上过来的dp
                        同理上边是障碍物那么当前dp=障碍物dp+从左过来的dp=从左过来的dp
                        最后上边和左边均为障碍物，dp=0+0=0
        """
        dp = [[0 for i in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]
        dp[0][0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                # 当前位置不是障碍, 障碍为位置对应的dp[i][j]永远为0，因此在下面加上也无所谓
                if obstacleGrid[i][j] != 1:
                    if i > 0 and j > 0:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]  # 非边界位置，因此它可以是从上边来的，可以是从左边来的
                    elif i > 0:  # 位于左边界  从上一个点过来只能往下走
                        dp[i][j] = dp[i - 1][j]
                    elif j > 0:  # 位于上边界 从上一个点过来只能往右走
                        dp[i][j] = dp[i][j - 1]
                # 当前位置是障碍的情况
                else:
                    dp[i][j] = 0

        return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsWithObstacles(obstacleGrid = [[0,1],[0,0]]))