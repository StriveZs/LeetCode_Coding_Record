---
title: LeetCode No.18

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第十八题
没做出来，首先用暴力肯定是timeout的，对于本体感觉就是在之前题目三数相加的基础上增加了一个外循环，采用双重外循环+双向指针来实现的，双向指针的目的在于将 o(n*n)的时间复杂度转换为o(n)。
## 题目描述
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。
```
示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
```

## 解题思路
自己修改之前的三数的代码，总是存在timeout的情况，于是就参考了评论区带佬的代码，增加了剪枝的操作，下面是解析：  

- 四数之和和三数之和思路类似。
- 三数之和是外层循环+内部双指针，四数就是外部两层循环+内部双指针；
- 先排序，去重思路还是一样的，外部两层每次判断和前一个数字相同就跳过，内部双指针移动同理判断；
- 增加一些剪枝策略，大大提高了执行用时；四处剪枝作用在外部两层循环，首先是在固定了第一个数的位置之后，如果这个数+最后一个数的三倍都还比target小，那么同样可以跳过此轮循环了；如果这个数+其后一个数的三倍比target都大，那么可以退出该层循环了；因为数组都是按升序排列的。
- 那么第二层的循环用来固定第二个数的位置时，同样可以用类似的逻辑进行判断，进行剪枝。

## 代码
```
class Solution:
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        res = []
        nums = sorted(nums)
        for i in range(len(nums)-3):
            # 1) 去重复
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 2) 剪枝第一处，因为i后面位置的元素是递增排序的。
            if nums[i] + 3*nums[i+1] > target:
                break
            # 3) 剪枝第二处，因为i后面位置的元素是递增排序的。
            if nums[i] + 3*nums[-1] < target:
                continue
            for j in range(i + 1, len(nums)-2):
                # 4) 去重复
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # 5) 剪枝第三处
                if nums[i]+nums[j]+2*nums[j+1] > target:
                    break
                # 6) 剪枝第四处
                if nums[i]+nums[j]+2*nums[-1] < target:
                    continue
                low, high = j + 1, len(nums) - 1
                while low < high:
                    if nums[i] + nums[j] + nums[low] + nums[high] == target:
                        res.append([nums[i], nums[j], nums[low], nums[high]])
                        low, high = low + 1, high - 1
                        # 7) 去重复
                        while low < high and nums[low] == nums[low - 1]:
                            low += 1
                        # 8) 去重复
                        while low < high and nums[high] == nums[high + 1]:
                            high -= 1
                    if nums[i] + nums[j] + nums[low] + nums[high] > target:
                        high -= 1
                    if nums[i] + nums[j] + nums[low] + nums[high] < target:
                        low += 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1, 0, -1, 0, -2, 2],0))
```