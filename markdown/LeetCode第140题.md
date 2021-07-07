---
title: LeetCode No.140

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第140题—单词拆分II
这几天课比较多，有点忙，可能来不及更新喔

自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：

分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
```
示例 1：

输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]
示例 2：

输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。
示例 3：

输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出:
[]
```
## 代码
```
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
```