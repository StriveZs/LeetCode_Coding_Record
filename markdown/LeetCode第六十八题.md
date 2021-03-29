---
title: LeetCode No.68

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第六十八题—文本左右对齐
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

最近写的花时间最久的一道题了。

## 题目描述
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

说明:

单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。

```
示例:

输入:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
示例 2:

输入:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
输出:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
     因为最后一行应为左对齐，而不是左右两端对齐。       
     第二行同样为左对齐，这是因为这行只包含一个单词。
示例 3:

输入:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
输出:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
```

## 代码
花了一个小时写了个模拟，感觉浪费我的时间了。 debug了半天哭哭哭 执行用时：40 ms, 在所有 Python3 提交中击败了56.62%的用户内存消耗：14.8 MB, 在所有 Python3 提交中击败了92.68%的用户

```
import re
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        核心思想：
                大模拟吧
                几点要求：
                    1. 每行恰好有 maxWidth 个字符
                    2. 左右两端对齐的文本
                    3. (贪心)尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。
                    4. 尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数
                    5. 文本的最后一行应为左对齐，且单词之间不插入额外的空格
                    6. 两个单词之间最少有一个空格

                一行一行的处理，每一行尽可能的多放置单词(模拟，即放置单词总长度+最少空格数<=maxWidth
                上述情况在多放一个单词就放不下了)
        """
        index = 0 # 单词坐标
        result = [] # 结果存放
        temp = '' # 当前行
        while index != len(words):
            # 如果当前单词长度直接等于maxWidth，则直接添加进去
            if len(words[index]) == maxWidth:
                result.append(words[index])
                index += 1
                continue
            # 处理一行，计算它能够存储多少个单词 找到那个单词的下标
            record_index = len(words)-1 # 记录它能够存储到单词的index  如果最后结果为len(words)+1的情况，则表示剩下的所有单词都可以被一行包括了
            record_len = 0 # 记录最大长度
            length = 0
            for i in range(index,len(words)):
                if i == index:
                    length += len(words[i]) # 首个单词
                else:
                    length = length + 1 + len(words[i]) # 其余单词都是 空格+单词形式  先默认都是一个空格的形式
                if length > maxWidth:
                    record_index = i - 1 # 记录下标
                    record_len = length - len(words[i]) - 1 # 记录长度
                    break
            # 特殊处理剩下的单词都被一行包括的情况(为最后一行的处理)
            if record_index == len(words) - 1:
                for i in range(index,record_index+1):
                    if i == index:
                        temp += words[i]
                    else:
                        temp = temp + ' ' + words[i]
                l_blank = [' ' for i in range(maxWidth - len(temp))]
                s_blank = ''.join(l_blank) # 在最后补充缺失的空格
                temp = temp + s_blank
                result.append(temp)
                index = record_index + 1
                temp = ''
            else: # 通常情况处理
                num_blank = maxWidth - record_len # 计算除了已经包含在内的单个空格数量之外还需要添加多少个空格
                num = record_index - index + 1 # 当前行可以包含的单词数量
                # 从左到右依次分配空格即可 就可以满足左边空格数大量大于右边空格数量 比如 还缺3个空格  当前temp=1 2 3 只需要按照这样步骤分配：1  2 3(左2 右1) -> 1  2  3(左2 右2) -> 1   2  3(左3 右2)分配即可
                for i in range(index,record_index+1):
                    if i == index:
                        temp = temp + words[index]
                    else:
                        temp = temp + ' ' + words[i]
                # 处理空格
                j = index
                curr_len = 0
                t_len = 0 # 临时长度 表示已经访问过的长度 用于下面寻找匹配字符串开头
                for i in range(num_blank):
                    # 考虑使用正则表达式来匹配字符串
                    t_i = temp.index(words[j],t_len)
                    curr_len = t_i + len(words[j])
                    t_len = t_i + len(words[j])
                    temp = temp[0:curr_len] + ' ' + temp[curr_len:]
                    t_l = len(temp)
                    j += 1
                    if j >= record_index:
                        j = index
                        t_len = 0
                result.append(temp)
                index = record_index + 1
                temp = ''
        return result

if __name__ == '__main__':
    s = Solution()
    res = s.fullJustify(["What","must","be","acknowledgment","shall","be"],16)
    print(res)
    print(len(res[2]))



```