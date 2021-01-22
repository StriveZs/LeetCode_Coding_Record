---
title: LeetCode No.17

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第十七题
## 题目描述
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

![figure.1](https://gitee.com/zyp521/upload_image/raw/master/SQXdUG.jpg)

```
示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

## 代码
```
import itertools

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        # 字典查表
        numList = ['2','3','4','5','6','7','8','9']
        characterList = [['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        temp = zip(numList,characterList)
        dictList = dict(temp)
        #print(dictList)

        digitsList = list(digits)
        numCharaList = []
        sumRes = 1
        # 统计输入的数字对应的字母
        for i in range(len(digitsList)):
            numCharaList.append(dictList[digitsList[i]])
        #print(numCharaList)

        # 生成结果
        result = []
        temp = list(itertools.product(*numCharaList))  # 调用库来生成列表排列组合
        for i in range(len(temp)):
            str1 = ''
            for j in range(len(list(temp[i]))):
                str1 += temp[i][j]
            result.append(str1)
        return result



if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('23'))
```