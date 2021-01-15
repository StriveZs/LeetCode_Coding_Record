---
title: LeetCode No.3

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第三题
## 题目描述
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

```
示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0
 
```

提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成

## 代码
### Python版本
#### 第一版
感觉自己严重缺乏OJ练习了，思想已经逐渐僵化，这一版直接超时了，虽然能做出来，但是不AC有卵用呢？  

```
import re

class Solution(object):
    def noRepeat(self,str1):
        """
        判断字符串是否存在重复字符
        :param str1:
        :return: Bool
        """
        flag = True
        for i in range(len(str1)):
            l1 = re.findall(str1[i],str1)
            if len(l1) != 1:
                flag = False
        return flag

    def cut(self, str1):
        """
        得到字符串的所有子串
        :type str1: str
        :return: list
        """
        results = []
        num = 0
        # x + 1 表示子字符串长度
        for x in range(len(str1)):
            # i 表示偏移量
            for i in range(len(str1) - x):
                tempStr = str1[i:i + x + 1]
                if self.noRepeat(tempStr):
                    results.append(tempStr)
        return results

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # print(self.cut(s))
        split_str = self.cut(s)
        maxLen = 0
        for i in range(len(split_str)):
            pattern = split_str[i]
            if re.search(pattern,s) != None:
                if len(pattern) > maxLen:
                    maxLen = len(pattern)
        return maxLen
```

#### 第二版
这一版是看了一下题解自己写的, 思想还是很简单的，是我太菜了。

```
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans;
```

### C艹版本
主要用的是vector来进行操作的, C++ 我都快忘光了，害 科研狗的噩梦。

```
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxLen=0,len=0;;
        vector<char> charV;
        int i=0,num=0;
        while(num < s.length()){
            if(find(charV.begin(),charV.end(),s[i]) == charV.end() && i<s.length()){
                charV.push_back(s[i]);
                len++;
            }
            else{
                num++;
                i = num;
                charV.clear();
                charV.push_back(s[i]);
                if(maxLen < len){
                    maxLen = len;
                }
                len = 1;
            }
            i++;
        }
        if(maxLen < len){
            maxLen = len;
        }
        return maxLen;
    }
};
```
