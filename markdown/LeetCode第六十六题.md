---
title: LeetCode No.66

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第六十六题
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

```

示例 1：

输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
示例 2：

输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。
示例 3：

输入：digits = [0]
输出：[1]
 

提示：

1 <= digits.length <= 100
0 <= digits[i] <= 9
```

## 代码
两种方法一个是在内存上击败90%的人，一个是在时间上击败98%的人
### 内存上

```
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]

        核心思想：
                就是将数字转换为对应的数字，然后加1，再将其转换为列表
                剪枝：对于尾数不为9的情况，直接在尾数加1返回即可
                    如果为9的话，则再转换为数字后加1再逆变换集合

                另外还有一种思想：在原数组上直接考虑进位即可，如果9+1的话原位等0，进1如果前一位不为9则直接上即可
                            如果为9则重复上述直到加到最高位的话，则直接在结果前插入1即可。
        """
        if digits[-1] != 9:
            digits[-1] = digits[-1] + 1
            return digits
        str1 = ''
        for i in range(len(digits)):
            str1 += str(digits[i])
        temp = str(int(str1) + 1)
        result = []
        for i in range(len(temp)):
            result.append(int(temp[i]))
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([9]))
```

### 时间上
```
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]

        核心思想：
                就是将数字转换为对应的数字，然后加1，再将其转换为列表
                剪枝：对于尾数不为9的情况，直接在尾数加1返回即可
                    如果为9的话，则再转换为数字后加1再逆变换集合

                另外还有一种思想：在原数组上直接考虑进位即可，如果9+1的话原位等0，进1如果前一位不为9则直接上即可
                            如果为9则重复上述直到加到最高位的话，则直接在结果前插入1即可。
        """
        i = len(digits)-1
        while digits[i] == 9:
            digits[i] = 0
            i -= 1
        if i == -1:
            digits = [1] + digits
        else:
            digits[i] += 1
        return digits
```