---
title: LeetCode No.49

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第四十九题
## 题目描述
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:
```
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。
```

## 代码
```
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]

        核心思想:
                第一种思路: 个人理解，首先对列表内容排序
                然后遍历列表中所有的字符串，将字母相同但是异位分别放在不同的列表中
                可以考虑使用字典统计

                第二种思路：首先我想到的是对每个字母赋值，然后计算每个字符串的总和，但是发现这样可能不同的字符串组合也会有相同的值
                因此考虑对每个字符串进行单独排序，然后判断他是否在里面，如果在则添加进去，如果不在则接着判断知道没有再创建一个新的
        """
        strs = sorted(strs)
        result = []
        judge_list = []
        # tt = strs[0]
        # tt = sorted(tt)
        # print(''.join(tt))
        # print(strs[0])
        for i in range(len(strs)):
            tt = strs[i]
            tt = ''.join(sorted(tt))
            if len(result) == 0:
                judge_list.append(tt)
                temp = []
                temp.append(strs[i])
                result.append(temp)
            else:
                if tt not in judge_list:
                    judge_list.append(tt)
                    temp = []
                    temp.append(strs[i])
                    result.append(temp)
                else:
                    index = judge_list.index(tt)
                    result[index].append(strs[i])
        return result






if __name__ == '__main__':
    s = Solution()
    s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
```