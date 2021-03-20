---
title: LeetCode No.60

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第六十题
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)
## 题目描述
给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
```
"123"
"132"
"213"
"231"
"312"
"321"
```
给定 n 和 k，返回第 k 个排列。

 
```
示例 1：

输入：n = 3, k = 3
输出："213"
示例 2：

输入：n = 4, k = 9
输出："2314"
示例 3：

输入：n = 3, k = 1
输出："123"
 

提示：

1 <= n <= 9
1 <= k <= n!
```

## 代码
### 回溯法超时版本
理论剪去达到k之后所有循环应该不会超时的，但还是超时了。  
```
from goto import with_goto
class Solution(object):
    # 计数菌
    jishuqi = 0
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str

        核心思想：这里Python有现成的库可以进行，但是为了能够掌握代码，这里我使用回溯法进行编写代码
                然后返回第k个结果

        回溯法的框架：
            def backtrack(path, selected):
                if 满足停止条件：
                    res.append(path)
                for 选择 in 选择列表：
                    做出选择
                    递归执行backtrack
                        满足则return True
                    如果不满足要求就撤销选择
        """
        result = []
        temp = []
        nums = [i+1 for i in range(n)]
        def backtrack(nums,k):
            if self.jishuqi == k:
                return
            if not nums:  # 如果为空则表示选择完毕
                if nums in result:
                    return False
                else:
                    self.jishuqi += 1
                    result.append(temp[:])
                    return True
            for i in range(len(nums)):
                # 做出选择
                temp.append(nums[i])
                # 去除做出的选择
                tt = nums[:i] + nums[i + 1:]
                # 接着执行选择
                backtrack(tt,k)
                # 撤销选择
                temp.pop()

        backtrack(nums,k)
        res = ''
        for i in range(len(result[-1])):
            res += str(result[-1][i])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(n=9,k=54994))
```

### 参考大佬的做法
```
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        s, k, res = list(range(1, n+1)), k-1, ""
        for i in range(len(s)-1, -1, -1):
            res, s, k = res+str(s[k // factorial(i)]), s[:k // factorial(i)]+s[k // factorial(i)+1:], k % factorial(i)
        return res
```