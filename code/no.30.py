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