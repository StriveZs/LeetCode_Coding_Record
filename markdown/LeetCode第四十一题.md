---
title: LeetCode No.41

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第四十一题
## 题目描述

给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

 

进阶：你可以实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案吗？

```
示例 1：

输入：nums = [1,2,0]
输出：3
示例 2：

输入：nums = [3,4,-1,1]
输出：2
示例 3：

输入：nums = [7,8,9,11,12]
输出：1
 

提示：

0 <= nums.length <= 300
-231 <= nums[i] <= 231 - 1
```

## 代码
```
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        核心思想:
                对列表进行遍历，然后对大于等于0的正整数创建字典, 没出现的正整数键值对应的为1
                然后从1开始访问字典，如果当前键值不存在则为没有出现的最小的正整数
        """
        temp = []
        maxNum = -1 # 最大值正整数
        for i in range(len(nums)):
            if nums[i] > 0:
                temp.append(nums[i])
                if nums[i] > maxNum:
                    maxNum = nums[i]
        # 解决 最大正整数过大的情况
        if maxNum >= len(temp):
            maxNum = len(temp)
        # 解决无正整数的情况
        if temp == []:
            return 1
        keyList = [i for i in range(maxNum+2)]  # 键值列表
        valueList = []  # 键值对应值的列表
        for i in range(maxNum+2):
            if i not in temp:
                valueList.append(-1)
            else:
                valueList.append(i)

        numsDict = dict(zip(keyList,valueList)) # 对应的字典
        #print(numsDict)
        index = -1
        for i in range(1,maxNum+2):
            if numsDict[i] == -1:
                index = i
                break
        return index

if __name__ == '__main__':
    s = Solution()
    print(s.firstMissingPositive(nums = [1,2,3,10,2147483647,9]))

```