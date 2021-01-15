---
title: LeetCode No.1

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

很久没有更新博客了之前一直在忙于考试，最近终于考完了，以后会慢慢坚持更新博客的。对于OJ这个题我计划是每天做一道两道，也是为了以后毕业可以在面试的时候有一个加分项吧，同样也可以锻炼一下自己的编程能力西西。  我觉得对于我来说就是贵在坚持，毕竟在果壳的科研路上也才刚刚起步，日久天长，在搞好科研的同时，可以在在其他方面提升一下自己。 

# LeetCode第1题
## 题目描述
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案。

```
示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]
```

## 代码
```
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result_index = []
        flag = False
        length = len(nums)
        for i in range(length):
            j = i+1
            while j < length:
                if nums[i] + nums[j] == target:
                    flag = True
                    result_index.append(i)
                    result_index.append(j)
                    break
                j = j + 1
            if flag:
                break
        return result_index

if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    s = Solution()
    print(s.twoSum(nums,target))

```