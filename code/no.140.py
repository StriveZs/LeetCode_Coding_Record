class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        还是使用动态规划，生成所有的可以拆分出来的字符串列表，然后在使用回溯法对这个字符串列表进行dfs找到所有满足条件的结果
        直接用回溯法的，感觉会time out 还是先用动态规划划分一下，在回溯吧
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        dp = [False] * (len(s)+1)
        dp[0] = True
        generate_word_list = [] # 存储结果
        for i in range(len(s)):
            if dp[i]:
                for j in range(i + 1, len(s) + 1):
                    if s[i:j] in wordDict:
                        dp[j] = True
                        generate_word_list.append(s[i:j])
        # 处理不可解
        if dp[-1] == False:
            return []
        # 回溯法
        res = []
        def back_track(index, temp, isEqualStr, s):
            if len(isEqualStr) > len(s):
                return
            if isEqualStr == s and temp not in res:
                res.append(temp)
            for i in range(index, len(generate_word_list)):
                temp_before = temp  # 用于回溯
                if temp == '':
                    temp = generate_word_list[i]
                else:
                    temp = temp + ' ' + generate_word_list[i]
                back_track(i+1, temp, isEqualStr+generate_word_list[i], s)
                # 撤回
                temp = temp_before

        back_track(0, '', '', s)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak("aaaaaaa",["aaaa","aaa"]))