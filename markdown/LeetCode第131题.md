---
title: LeetCode No.131

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第131题—分隔回文串

昨天端午鸽了塞

自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

回文串 是正着读和反着读都一样的字符串。

```
示例 1：

输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
示例 2：

输入：s = "a"
输出：[["a"]]
 
提示：

1 <= s.length <= 16
s 仅由小写英文字母组成
```

## 代码
```
import copy
class Solution(object):
    res = []
    # fixme:判断是否是回文串
    def isPalindrome(self, s):
        if s == s[::-1]:
            return True
        return False

    def partition(self, s):
        """
        最终的结果，每个字符单独拿出来肯定是一个回文串, 因此不存在空字符串结果的情况，除非输入就是空串
        算法考虑的话，有两种方法:
            1. 动态规划
            2. 回溯法
        :type s: str
        :rtype: List[List[str]]
        """
        self.res = []
        # 回溯法
        def backtrack(s, path):
            if len(s) == 0:
                tt = copy.copy(path) # 如果直接用self.res.append(path)的话，由于是浅拷贝，后面再path.remove的话，res中的结果也会被修改
                self.res.append(tt)
            for i in range(1, len(s) + 1):  # 注意起始和结束位置
                if self.isPalindrome(s[:i]):
                    path.append(s[:i])
                    backtrack(s[i:], path)
                    path.remove(s[:i])
        backtrack(s,[])
        return self.res

if __name__ == '__main__':
    s = Solution()
    print(s.partition("a"))
```

### 更加推荐的写法
```
class Solution(object):
    # fixme:判断是否是回文串
    def isPalindrome(self, s):
        if s == s[::-1]:
            return True
        return False

    def partition(self, s):
        """
        最终的结果，每个字符单独拿出来肯定是一个回文串, 因此不存在空字符串结果的情况，除非输入就是空串
        算法考虑的话，有两种方法:
            1. 动态规划
            2. 回溯法
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        # 回溯法
        def backtrack(s, res, path):
            if not s:
                res.append(path)
                return
            for i in range(1, len(s) + 1):  # 注意起始和结束位置
                if self.isPalindrome(s[:i]):
                    backtrack(s[i:], res, path + [s[:i]])
        backtrack(s,res,[])
        return res
```