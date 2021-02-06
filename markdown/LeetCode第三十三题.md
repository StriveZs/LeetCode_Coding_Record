---
title: LeetCode No.33

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第三十三题
昨天这题没写完，无限火力太好玩了 md，今天又花了一个小时写完了。太菜了

## 题目描述
升序排列的整数数组 nums 在预先未知的某个点上进行了旋转（例如， [0,1,2,4,5,6,7] 经旋转后可能变为 [4,5,6,7,0,1,2] ）。

请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

 
```
示例 1：

输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
示例 2：

输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
示例 3：

输入：nums = [1], target = 0
输出：-1
 

提示：

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
nums 中的每个值都 独一无二
nums 肯定会在某个点上旋转
-10^4 <= target <= 10^4
```

## 代码
给我写吐血了，写了两个小时，我太菜了，连二分查找都快忘了。最终还是AC了 害 辛苦没白费。

```
class Solution(object):
    # 递归寻找旋转点  二分法
    def searchMidPoint(self,nums,l,r):
        if r <= l+1:
            return l+1
        else:
            mid = int((r+l)/2)
            if nums[mid] < nums[len(nums)-1]:
                return self.searchMidPoint(nums, l, mid)
            else:
                return self.searchMidPoint(nums, mid, r)

    # 二分法寻找目标值
    def binarySearch(self,nums, l, r, target):
        if r > l:
            mid = int((r+l)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return self.binarySearch(nums, l, mid - 1, target)
            else:
                return self.binarySearch(nums, mid + 1, r, target)
        elif r == l:
            if nums[r] == target:
                return r
            else :
                return -1
        else:
            return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        旋转数组：
                输入: [1,2,3,4,5,6,7] 和 k = 3
                输出: [5,6,7,1,2,3,4]
                解释:
                向右旋转 1 步: [7,1,2,3,4,5,6]
                向右旋转 2 步: [6,7,1,2,3,4,5]
                向右旋转 3 步: [5,6,7,1,2,3,4]
        核心思想：采用二分搜索法
                对于num来说，如果它的最后侧的数比中间数大则中间数右侧的序列是有序的，而左侧则是无序的
                然后以此来找左侧的数组中的中间数同样进行判断，采用递归的方法来寻找到旋转点
                找到旋转点后就可以将原数组划分为两个序列，分别对两个序列进行二分查找从而找到对应的下标
        """
        # 特殊处理 nums 长度为1或2
        if len(nums) <= 2:
            if nums[0] == target:
                return 0
            else:
                if len(nums) == 2 and nums[1] == target:
                    return 1
                else:
                    return -1
        # 创建字典来对应对下标
        # index = list(range(len(nums)))
        # indexlist = dict(zip(nums,index))
        # print(indexlist)
        # 寻找旋转点
        if nums[0] < nums[len(nums)-1]:
            index = len(nums)
        else:
            index = self.searchMidPoint(nums, 0, len(nums) - 1)  # 旋转点
        if index == 0:
            index += 1
        #print(index)
        # 找到旋转点之后就可以将原数组划分为两个有序数组
        leftlist = nums[0:index]
        rightlist = nums[index:len(nums)]
        print(leftlist)
        print(rightlist)
        # 如果target大于leftlist则在nums中则位于leftlist，反之如果targe小于leftlist大于rightlist则在rightlist中
        if len(rightlist) == 0:
            if target < leftlist[0] and target > leftlist[len(leftlist)-1]:
                return -1
            else:
                tarIndex = self.binarySearch(leftlist, 0, len(leftlist) - 1, target)
                return index - len(leftlist) + tarIndex
        else:
            if target >= leftlist[0] and target <= leftlist[len(leftlist) - 1]:
                tarIndex = self.binarySearch(leftlist, 0, len(leftlist) - 1, target)
                if tarIndex == -1:
                    return - 1
                return index - len(leftlist) + tarIndex
            elif target >= rightlist[0] and target <= rightlist[len(rightlist) - 1]:
                tarIndex = self.binarySearch(rightlist, 0, len(rightlist) - 1, target)
                if tarIndex == -1:
                    return - 1
                return tarIndex + index
            else:
                return -1

if __name__ == '__main__':
    s = Solution()
    print(s.search(nums = [4,5,6,7,0,1,2], target = 2))

```