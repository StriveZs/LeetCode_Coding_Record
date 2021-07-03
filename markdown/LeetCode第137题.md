---
title: LeetCode No.137

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第137题—只出现一次的数字II
今天获得了习近平七年知青岁月这本书，很开心！

自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

```

示例 1：

输入：nums = [2,2,3,2]
输出：3
示例 2：

输入：nums = [0,1,0,1,0,1,99]
输出：99
 

提示：

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次
 

进阶：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
```

## 代码
```
class Solution(object):
    def singleNumber(self, nums):
        """
        还是考虑使用以前的异或操作，这里建立一个记忆字典，如果一个数出现了3次，则本次异或运算该数不参与运算了
        所有的数只能出现3次或者1次，而且只有一个数可以出现1次 (充分利用这个思想)
        然后就可以按照上一题的思路来做了:
        异或^:
            n ^ n = 0
            0 ^ n = n
        :type nums: List[int]
        :rtype: int
        """
        memory = dict()
        res = nums[0]
        memory[res] = 1 # 出现次数设为1
        for i in range(1, len(nums)):
            if nums[i] not in memory.keys():
                memory[nums[i]] = 1
            else:
                memory[nums[i]] += 1
            # 出现第三次就跳过
            if memory[nums[i]] == 3:
                continue

            res = res ^ nums[i]
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([2,2,3,2]))
```