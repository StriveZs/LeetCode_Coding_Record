---
title: LeetCode No.5

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第五题
## 题目描述
给你一个字符串 s，找到 s 中最长的回文子串。

 
```
示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
示例 3：

输入：s = "a"
输出："a"
示例 4：

输入：s = "ac"
输出："a"
 

提示：

1 <= s.length <= 1000
s 仅由数字和英文字母（大写和/或小写）组成
```

## 代码
### Python
这个版本超时了，原因分析的话：应该是划分子串操作timeout了。  

```
    def cut(self, str1):
        """
        得到字符串的所有子串
        :type str1: str
        :return: list
        """
        results = []
        # x + 1 表示子字符串长度
        for x in range(len(str1)):
            # i 表示偏移量
            for i in range(len(str1) - x):
                tempStr = str1[i:i + x + 1]
                results.append(tempStr)
        return results


    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        split_res = self.cut(s)
        length = len(split_res)
        maxlen = 0
        result = ''
        for i in range(length):
            temp = split_res[length - i - 1][::-1] # 字符串翻转
            if temp == split_res[length - i - 1]:
                if len(temp) > maxlen:
                    maxlen = len(temp)
                    result = split_res[length - i - 1]

        return result
```

### C++
AC的C++版本

```
#include <string.h>
#include <vector>
class Solution {
public:
    string longestPalindrome(string s) {
        int len = s.length();
        if(len == 0 || len == 1){
            return s;
        }
        int start=0;
        int maxLen = 1;
        vector<vector<int> > ls(len,vector<int>(len)); //定义一个二维数组
        //初始化找一个长度为2的字符串的回文  s[i] = s[i+1]
        for(int i=0;i<len;i++){
            ls[i][i] = 1;
            if(i < len-1 && s[i] == s[i+1]){
                ls[i][i+1] = 1;
                maxLen = 2;
                start = i;
            }
        }
        //接下来处理长度大于2 小于最大长度的回文
        for(int i = 3;i<=len;i++){
            for(int j=0;j+i-1<len;j++){
                int ends = j+i-1; //终止字符位置  长度为i的字符串
                if(s[j] == s[ends] && ls[j+1][ends-1] == 1){ //满足首位字符相同，且长度为i-1的字符串也是回文串
                    ls[j][ends] = 1;
                    start = j;
                    maxLen = i;
                }
            }
        }
        return s.substr(start,maxLen);
    }
};
```