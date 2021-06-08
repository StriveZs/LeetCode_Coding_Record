---
title: LeetCode No.128

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第128题—最长连续序列
好久没更新了，最近事情太多了，天天忙的要死，英语也没来得及背，后面会慢慢恢复的，同时也会更新一大堆学习到的东西，敬请期待。  

自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

进阶：你可以设计并实现时间复杂度为 O(n) 的解决方案吗？

```

示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
 

提示：

0 <= nums.length <= 104
-109 <= nums[i] <= 109

````
## 代码
```
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        核心思想:
            考虑用字典存储当前长度
            dict[a] = b 表示这个每个端点值对应连续区间的长度
            键值是顺序从小到大的
        """
        max_length = 0
        res_dict = dict()
        for num in nums:
            # 去掉重复情况
            if num not in res_dict.keys():
                # 找到它的左端值和右端值
                left_length = res_dict.get(num-1,0) # 如果左边值存在则和左边值连续，否则返回0
                right_length = res_dict.get(num+1,0) # 如果右边值存在，则和右边值连续，否则返回0
                length = left_length + right_length + 1
                if length > max_length:
                    max_length = length
                # 更新字典值
                res_dict[num] = length
                # 更新左邻域最大长度(没有的话不更新)
                res_dict[num-left_length] = length
                # 更新有邻域最大长度(如果没有的话，则不更新)
                res_dict[num+right_length] = length
        return max_length

```