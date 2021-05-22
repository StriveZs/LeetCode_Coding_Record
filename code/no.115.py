class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int

        核心思想:

            字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。
            （例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是
            动态规划和递归的区别:
                dp是一种不带重复计算的递归，想出dp往往也是像想出递归那样，都需要从子问题入手，正确定义子问题，递归想出结束条件，
                dp想出base case，递归想出递归公式，dp想出递推公式。递归加入记忆化后，
                往往稍作修改，就是dp的解法

            考虑使用二维动态规划
            dp[i][j]：从开头到s[i-1]的子串中，出现『从开头到t[j-1]的子串』的 次数。
            即：前i个字符的s子串中，出现前j个字符的t子串的次数。
        """
        len_s = len(s)
        len_t = len(t)
        dp = [[0] * (len_s + 1) for i in range(len_t+1)] # 生成dp数组, +1是为了考虑空串的情况
        # print(dp)
        # 当t的子字符串为空字符串时
        for i in range(len_s + 1):
            dp[0][i] = 1
        for i in range(1,len_t+1):
            for j in range(1,len_s+1):
                # 当s的子字符串为空字符串时
                # s为空串，无论怎么删去元素，s还是无法变成t
                # 处理其他情况
                # 数组i不变j+1的时候，这时就相当于s增加了一个元素，以s='ba' t='b'为例
                # 此时dp[1][2]=1，j要加1变成dp[1][3]了，这时s就变成了'bab'
                # 因此需要判断t[i]和新增的s[j+1]是否相等，如果不等的话，则dp[i][j+1]=dp[i][j]
                # 如果相等的话，同时去掉i和j+1分别看剩下的s和t是否有多个匹配，因此dp[i][j+1] = dp[i][j]+dp[i-1][j]
                if s[j-1] == t[i-1]: # -1是因为上面循环算上了""字符串的情况
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]

        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.numDistinct(s = "rabbbit", t = "rabbit"))