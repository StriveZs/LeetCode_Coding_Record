class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        拆分时可以重复使用字典中的单词。
        你可以假设字典中没有重复的单词
        题目分析:
            从头到尾开始移动index，进行单词切片，如果单词在字典里就，从新的index开始
            这种做法无法解决: "goalspecial"  ["go","goal","goals","special"] 这种情况
        因此需要考虑动态规划的做法：
            dp[i] 表示前i个字符是否能够拆分成wordDict
            状态转移公式:
                dp[i]=true的话，则只需要判断i+1到j个字符是否属于WordDict就可以了
            最后返回dp[-1]就好了
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s)+1) # dp[]长度为len(s)+1
        dp[0] = True # 设置初始
        for i in range(len(s)):
            if dp[i]:
                for j in range(i+1, len(s)+1):
                    if s[i:j] in wordDict:
                        dp[j] = True
                        # 提前结束条件
                        if j == len(s)+1:
                             return True
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak("catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))