---
title: LeetCode No.78

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第七十八题—组合
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

```

示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]
 

提示：

1 <= nums.length <= 10
-10 <= nums[i] <= 10
nums 中的所有元素 互不相同
```

## 代码
回溯法，5分钟改了一下上道题的代码就搞定了。 执行结果：通过显示详情执行用时：44 ms, 在所有 Python3 提交中击败了36.44%的用户内存消耗：14.7 MB, 在所有 Python3 提交中击败了97.21%的用户
```
import copy
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        核心思想:
                同样是回溯法的应用
                相比较于上一题只不过是：k是可变的
                算法框架：
                    def backtrack(path, selected):
                        if 满足停止条件：
                            res.append(path)
                        for 选择 in 选择列表：
                            做出选择
                            递归执行backtrack
                                满足则return True
                            如果不满足要求就撤销选择
        """
        res = []
        res.append([])
        numsLen = len(nums)
        temp = []
        def backtrack(temp,l,numsLen,length):
            # 停止条件
            if len(temp) == length:
                if temp not in res:
                    tt = copy.copy(temp)
                    res.append(tt)
                    return

            for j in range(l+1,numsLen):
                # 做出选择
                temp.append(nums[j])
                # 递归执行
                backtrack(temp,j,numsLen,length)
                # 撤销选择
                temp.pop()
        # 递归调用  length值不同
        for i in range(1,numsLen+1):
            backtrack(temp, -1, numsLen,i)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.subsets(nums = [0]))
```