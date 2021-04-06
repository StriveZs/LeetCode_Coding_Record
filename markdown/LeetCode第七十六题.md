---
title: LeetCode No.76

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第七十六题—最小覆盖子串
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。

```

示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
示例 2：

输入：s = "a", t = "a"
输出："a"
 

提示：

1 <= s.length, t.length <= 105
s 和 t 由英文字母组成
```

## 代码
### 学习一手滑窗模板
```
lo, hi = 0, 0
while hi < n:
    window += grumpy[hi] * customers[hi]        # 右值进入窗口
    while hi - lo + 1 > X:                      # 维护大小为X的窗口
        window -= grumpy[lo] * customers[lo]    # 左值退出窗口
        lo += 1                                 # 左指针前进1
    <do...>                                     # 任务1
    hi += 1                                     # 右指针前进1
```
### Sliding Window
参考带佬的滑窗模板版本：
```
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ans = ''
        minLen = float('Inf')
        lo, hi = 0, 0
        window = Counter()
        t = Counter(t)
        while hi < len(s):
            # 入窗
            window[s[hi]] += 1
            # 维护窗口大小
            while all(map(lambda x: window[x] >= t[x], t.keys())):
                # 筛选符合条件的最短长度
                if hi - lo + 1 < minLen:
                    ans = s[lo:hi+1]
                    minLen = hi - lo + 1
                # 出窗
                window[s[lo]] -= 1
                lo += 1
            # 窗口右端右移
            hi += 1
        return ans
```

### 最后一个用例超时版本
感觉思路很清晰，一写就超时 妈的  
感觉可以在时间复杂度上得到很大的优化，比如统计信息等等。for 循环太多了

```
import copy
class Solution(object):
    def judge(self,Dict,tList):
        for i in range(len(tList)):
            if Dict[tList[i]] > 0:
                return False
        return True

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        
            核心思想:
                    采用双指针记录滑窗头尾位置
                    从头滑窗，如果t.split的每个字符串都在，则记录这个字符串
                    剪枝：如果滑窗的长度长于当前最短的长度则直接跳转到下一个属于t字母的位置重新进行滑窗
        """
        if len(t) > len(s):
            return ""
        if s == t:
            return s
        if len(s) == 1:
            if s == t:
                return s
            else:
                return ""
        windowStart = 0
        windowEnd = 0
        minLen = len(s)
        res = ''
        tList = list(t)
        # 生成每个字母的个数统计字典，然后后面用减法
        zeroList = [0 for i in range(len(tList))]
        staticDict = dict(zip(tList,zeroList)) # 创建查询字典 记录每个单词的个数
        for i in range(len(t)):
            staticDict[t[i]] += 1
        searchDict = copy.copy(staticDict) # 创建查询字典，用于下面减法
        #print(searchDict)
        while len(s) - windowStart >= len(t): # 如果可滑窗的范围小于t的长度，则结束循环
            if windowEnd == len(s): # 越界直接结束
                break
            temp = s[windowEnd]
            #print(temp)
            if s[windowEnd] in tList:
                searchDict[s[windowEnd]] -= 1  # 记录值＋1
                if self.judge(searchDict,tList): # 判断是否所有记录值均不为0
                    # 记录满足条件的更短字符串
                    if minLen >= windowEnd - windowStart + 1:
                        minLen = windowEnd - windowStart + 1
                        res = s[windowStart:windowEnd+1]
                    searchDict = copy.copy(staticDict) # 重置
                    flag = True
                    # 直接从下一个位于t中的字母开始
                    for i in range(windowStart+1,len(s)):
                        if s[i] in tList:
                            windowStart = i
                            flag = False
                            break
                    if flag:
                        break
                    # 新的开始 重置windowEnd
                    windowEnd = windowStart
                else:
                    windowEnd += 1
            else:
                windowEnd += 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.minWindow(s = "abc", t = "ac"))
```