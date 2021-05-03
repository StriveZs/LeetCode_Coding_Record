---
title: LeetCode No.97

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

五一出去旅游了，鸽了几天，回来接着更新塞。  

# LeetCode第九十七题—交错字符串
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。

两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
提示：a + b 意味着字符串 a 和 b 连接。

![figure.1](https://gitee.com/zyp521/upload_image/raw/master/EbJwpE.jpg)

```
示例 1：

输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出：true
示例 2：

输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出：false
示例 3：

输入：s1 = "", s2 = "", s3 = ""
输出：true
 

提示：

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1、s2、和 s3 都由小写英文字母组成
```

## 核心思想
我太菜了，真想不出来。参考大佬的作答。  

看成是一个寻找路径的问题。采用动态规划解决,如下图所示:

![figure.2](https://gitee.com/zyp521/upload_image/raw/master/gumBAx.jpg)

## 代码
```
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool

        核心思想:
                考虑最脑残的方法，直接对s1和s2的所有字母进行统计
                然后在对s3进行统计
                如果两种字母数量和类别不一样的话，则返回false
                否则返回true

                考虑使用字典存储

                上述方法失败，还要我忽略了还要保证顺序的问题

                如果s1的长度+s2的长度不等于s3的长度，则一定不行

                考虑使用动态规划来解决
                可以将本问题看成寻找路径的问题，dp[i][j]表示s1的前i个字符和s2的前j个字符是否可以构成s3前i+j个字符
                dp[0][0]为""和""
        """
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for i in range(len(s2)+1)] for j in range(len(s1)+1)] # 初始dp数组
        dp[0][0] = True
        # 先处理s2为""，s1不为""的情况
        for i in range(1,len(s1)+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        # 处理s1为""，s2不为""的情况
        for j in range(1,len(s2)+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        # s1和s2均不为""
        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))
```