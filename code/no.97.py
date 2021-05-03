class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool

        核心思想:
                考虑最脑残的方法，直接对s1和s2的所有字母进行统计
                然后在对s3进行统计
                如果两种字母数量和类别不一样的话，则返回false
                否则返回true

                考虑使用字典存储

                上述方法失败，还要我忽略了还要保证顺序的问题

                如果s1的长度+s2的长度不等于s3的长度，则一定不行

                考虑使用动态规划来解决
                可以将本问题看成寻找路径的问题，dp[i][j]表示s1的前i个字符和s2的前j个字符是否可以构成s3前i+j个字符
                dp[0][0]为""和""
        """
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for i in range(len(s2)+1)] for j in range(len(s1)+1)] # 初始dp数组
        dp[0][0] = True
        # 先处理s2为""，s1不为""的情况
        for i in range(1,len(s1)+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        # 处理s1为""，s2不为""的情况
        for j in range(1,len(s2)+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        # s1和s2均不为""
        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))