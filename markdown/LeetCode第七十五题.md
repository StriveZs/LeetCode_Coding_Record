---
title: LeetCode No.75

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第七十五题—颜色分类
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

```
示例 1：

输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]
示例 2：

输入：nums = [2,0,1]
输出：[0,1,2]
示例 3：

输入：nums = [0]
输出：[0]
示例 4：

输入：nums = [1]
输出：[1]
 

提示：

n == nums.length
1 <= n <= 300
nums[i] 为 0、1 或 2
```

## 代码
```
import copy
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        核心思想：
                考虑可以先用字符串存储结果，再将字符串转换为list
                如果为0则字符串+'0'，如果为1，则在字符串记录当前最后一个0的位置处加'1'，为2的话则直接在末尾加'2'
        """
        resStr = ''
        index0 = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                if index0 == -1:
                    index0 = 0
                else:
                    index0 = index0 + 1
                resStr = '0' + resStr
            elif nums[i] == 1:
                resStr = resStr[0:index0+1] + '1' + resStr[index0+1:]
            elif nums[i] == 2:
                resStr = resStr + '2'
        nums=copy.copy([ int(i) for i in list(resStr)])
        return nums

if __name__ == '__main__':
    s = Solution()
    print(s.sortColors([0,1,2]))
```