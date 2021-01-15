---
title: LeetCode No.4

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode 第四题
## 题目描述
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。

进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？

 

```
示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
示例 3：

输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000
示例 4：

输入：nums1 = [], nums2 = [1]
输出：1.00000
示例 5：

输入：nums1 = [2], nums2 = []
输出：2.00000
 

提示：

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
```

## 代码
### Python版本
```
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #print(nums1)
        nums1.extend(nums2)
        #print(nums1)
        nums1.sort()
        length = len(nums1)

        if length == 1:
            return nums1[0]
        elif length == 0:
            return 0
        elif length % 2 == 0:
            index1 = int(length / 2)
            index2 = index1 - 1
            return (nums1[index1] + nums1[index2]) / 2
        elif length % 2 == 1:
            index = int((length / 2))
            return nums1[index]
```

### C++
```
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<double> list;
        double result=0;
        for(int i=0;i<nums1.size();i++){
            list.push_back(nums1[i]);
        }
        for(int i=0;i<nums2.size();i++){
            list.push_back(nums2[i]);
        }
        sort(list.begin(),list.end());
        int len = list.size();
        if(len%2 == 0){
            int index1 = len/2;
            int index2 = index1 + 1;
            result = (list[index1-1] + list[index2-1]) / 2;
        }
        else{
            result = list[ceil(float(len)/2)-1];
        }
        return result;
    }
};
```