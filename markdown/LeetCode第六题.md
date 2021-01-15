---
title: LeetCode No.6

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第六题
本题的实质就是模拟，虽然AC了，但是空间复杂度有点高，时间复杂度的话就是O(len(s))主要是找不到一个合适的存储，我只能用numpy存储了，大小的话和numRow有关。  

## 题目描述
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
 
```
示例 1：

输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"
示例 2：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I
示例 3：

输入：s = "A", numRows = 1
输出："A"
 

提示：

1 <= s.length <= 1000
s 由英文字母（小写和大写）、',' 和 '.' 组成
1 <= numRows <= 1000
```

## 代码

稍微给个原理图:  

![figure.1](https://gitee.com/zyp521/upload_image/raw/master/O3gsTr.png)

```
import numpy as np

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        list_str = list(s)
        length = len(s)
        if numRows == 1:
            return s
        onePart = numRows + (numRows - 2) # 一个Z字形前半部分的字符个数
        numPart = int(length / onePart) + 1 # 总共多少个part
        #print(list_str)

        storeChart = np.zeros((numRows,numPart*numRows-1),dtype=np.string_) # 用来存储Z字形变换后的字符
        #print(storeChart)
        row = 0
        flag = False
        for i in range(length):  # 时间复杂度为O(len(s))
            if numRows == 2:  # 单独处理2这种情况
                if i % onePart == 0:
                    storeChart[i % onePart][row] = list_str[i]
                elif i % onePart == 1:
                    storeChart[i % onePart][row] = list_str[i]
                    row += 1
            elif i % onePart < numRows:
                if flag:
                    row += 1
                    flag = False
                storeChart[i % onePart][row] = list_str[i]
            elif i % onePart >= numRows:
                row += 1
                flag = True
                storeChart[onePart - i % onePart][row] = list_str[i]
        #print(storeChart)
        strList = storeChart.astype(np.str)
        result = ''
        for i in range(strList.shape[0]):
            for j in range(strList.shape[1]):
                if strList[i][j] != '':
                    result += str(strList[i][j])

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.convert('ABCD',2))
```