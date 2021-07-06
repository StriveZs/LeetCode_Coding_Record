---
title: LeetCode No.139

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第139题—单词拆分
这几天课比较多，有点忙，可能来不及更新喔

自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
```
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
```
## 代码
### 最初版本
```
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
            for j in range(i+1, len(s)+1):
                if dp[i]:
                    if s[i:j] in wordDict:
                        dp[j] = True
        return dp[-1]
```
### 加速和节省之后的版本
```
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
```