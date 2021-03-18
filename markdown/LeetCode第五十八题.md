---
title: LeetCode No.58

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第五十八题
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)
## 题目描述
给你一个字符串 s，由若干单词组成，单词之间用空格隔开。返回字符串中最后一个单词的长度。如果不存在最后一个单词，请返回 0 。

单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。

 
```
示例 1：

输入：s = "Hello World"
输出：5
示例 2：

输入：s = " "
输出：0
 

提示：

1 <= s.length <= 104
s 仅有英文字母和空格 ' ' 组成
```

## 代码
```
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        核心思想:
                python方法直接用split(' ')对字符串进行划分，返回list[-1]的长度即可
                注意考虑全是空格的情况
        """
        res = s.split(' ')
        #print(res)
        for i in range(len(res)):
            if res[len(res)-i-1] != '':
                return len(res[len(res)-i-1])
        return 0
if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord(s = "     "))
```