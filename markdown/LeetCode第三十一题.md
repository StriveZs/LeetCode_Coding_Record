---
title: LeetCode No.31

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第三十一题
## 题目描述
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须 原地 修改，只允许使用额外常数空间。

 
```
示例 1：

输入：nums = [1,2,3]
输出：[1,3,2]
示例 2：

输入：nums = [3,2,1]
输出：[1,2,3]
示例 3：

输入：nums = [1,1,5]
输出：[1,5,1]
示例 4：

输入：nums = [1]
输出：[1]
 

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 100
```

## 代码
```
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums) # 总长度
        index_a = length - 1
        # 从后往前找
        while index_a >= 0:
            index_b = length - 1
            while index_b > index_a :
                # 如果大于则交换位置并对前面查找的内容进行排序
                if nums[index_b] > nums[index_a]:
                    temp = nums[index_a]
                    nums[index_a] = nums[index_b]
                    nums[index_b] = temp
                    tt = nums[index_a + 1:len(nums)]
                    tt.sort()
                    nums[index_a+1:len(nums)] = tt
                    return nums
                index_b -= 1
            index_a -= 1
        nums.reverse()
        return nums

if __name__ == '__main__':
    s = Solution()
    print(s.nextPermutation(nums = [1,3,2]))
```