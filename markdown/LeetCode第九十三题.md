---
title: LeetCode No.93

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第九十三题—复原IP地址
## 题目描述
给定一个只包含数字的字符串，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。

有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。

```

示例 1：

输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
示例 2：

输入：s = "0000"
输出：["0.0.0.0"]
示例 3：

输入：s = "1111"
输出：["1.1.1.1"]
示例 4：

输入：s = "010010"
输出：["0.10.0.10","0.100.1.0"]
示例 5：

输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

提示：

0 <= s.length <= 3000
s 仅由数字组成
```

## 代码
执行用时：36 ms, 在所有 Python3 提交中击败了94.35%的用户内存消耗：14.9 MB, 在所有 Python3 提交中击败了86.32%的用户

好像可以缩减一下代码QWQ
```
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]

        核心思想:
                回溯算法
                def backtrack(path, selected):
                    if 满足停止条件：
                        res.append(path)
                    for 选择 in 选择列表：
                        做出选择
                        递归执行backtrack
                            满足则return True
                        如果不满足要求就撤销选择
                满足条件判断：
                    1. 位于0-255之间
                    2. 以0开头的不满足，比如：01 02 010等
                    3. 含有非法字符不满足
                    4. 划分部分必须等于4部分
                存储结构使用[]存储，将满足的[]在存到result中
        """
        self.res = []
        # 去除长度大于12的情况，因此长度大于12，属于非法的
        if len(s) > 12:
            return self.res
        # 回溯
        def backtrack(s, path):
            if len(path) == 4:
                if path not in self.res:
                    self.res.append('.'.join(path))
                    return
            # 已经选择了3个
            if len(path) == 3 and s != '':
                temp = s
                # 选择合法的情况
                if int(temp) >= 0 and int(temp) <= 255:
                    # 去除前导为0的情况，如果前导存在0，则不再进行递归
                    if str(int(temp)) == temp:
                        backtrack('',path+[temp])
            # 选择一个1或者两个或者0个的情况都是一样的
            elif len(path) < 3 and s != '':
                # 最大可选择的长度为3
                if len(s) <= 3:
                    for i in range(len(s)):
                        temp = s[:i+1]
                        next = s[i+1:]
                        if int(temp) >= 0 and int(temp) <= 255:
                            # 去除前导为0的情况，如果前导存在0，则不再进行递归
                            if str(int(temp)) == temp:
                                backtrack(next, path+[temp])
                else:
                    for i in range(3):
                        temp = s[:i + 1]
                        next = s[i + 1:]
                        if int(temp) >= 0 and int(temp) <= 255:
                            # 去除前导为0的情况，如果前导存在0，则不再进行递归
                            if str(int(temp)) == temp:
                                backtrack(next, path+[temp])
        backtrack(s, [])
        return self.res
                        
if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses("1111"))
```