---
title: LeetCode No.30

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第三十题
## 题目描述
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

```
示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]
```

## 代码
### 超时版本
采用最传统的办法直接超时了，裂开。  

```
import itertools

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        wordList = list(itertools.permutations(words, len(words))) # 调用库来生成列表排列组合
        stringList = []
        for i in range(len(wordList)):
            temp = ''
            for j in range(len(words)):
                temp += wordList[i][j]
            if temp not in stringList:
                stringList.append(temp)
        indexlist = []
        for i in range(len(s)):
            for j in range(len(stringList)):
                if i + len(stringList[j]) <= len(s):
                    if s[i:i + len(stringList[j])] == stringList[j]:
                        indexlist.append(i)
        return indexlist

if __name__ == '__main__':
    s = Solution()
    print(s.findSubstring(s = "barfoothefoobarman",
  words = ["foo","bar"]))

```

### AC版本
纯手撸，一个小时搞定，头大。

```
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        核心思想：
                ① 先统计words中每个单词的词频、words中单词的个数和一个单词的长度
                ② 然后从头开始遍历s，统计（单词数×单词长度）的长度内单词出现的次数
                ③ 如果在当前坐标下统计到的单词次数和words中单词词频相同则表示相同并记录index
        """
        # 统计words词频
        wordsnum = len(list(set(words)))
        zerolist = [0 for i in range(wordsnum)]
        wordsdicts = dict(zip(list(set(words)), zerolist))
        for i in words:
            wordsdicts[i] += 1
        # print(wordsdicts)
        # 记录string词频
        zerolist = [0 for i in range(wordsnum)]
        strdicts = dict(zip(list(set(words)),zerolist))
        # 组合后的长度
        wordnum = len(words)
        wordlength = len(words[0])
        sumlength = wordnum * wordlength
        # print(strdicts)
        # 下标存储list
        indexlist = []

        # 统计string
        for i in range(len(s)):
            # 更新词频
            zerolist = [0 for i in range(wordsnum)]
            strdicts = dict(zip(list(set(words)), zerolist))
            flag = True
            if i + sumlength > len(s):
                break
            else:
                t = i
                for j in range(wordnum):
                    if s[t:t+wordlength] in words:
                        strdicts[s[t:t+wordlength]] += 1
                        t += wordlength
                    else:
                        flag = False
                        break
                if flag:
                    flags = True
                    for k,v in strdicts.items():
                        if wordsdicts[k] != v:
                            flags = False
                            break
                    if flags:
                        indexlist.append(i)
        return indexlist

if __name__ == '__main__':
    s = Solution()
    print(s.findSubstring(s = "barfoothefoobarman",
  words = ["foo","bar"]))
```