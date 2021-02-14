---
title: LeetCode No.39

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第三十九题
好几天没写了，正过年休息了两天，今天把之前的补回来，新年快乐，牛年大吉奥。  

## 题目描述
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1：
```
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
示例 2：

输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
 

提示：

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
candidate 中的每个元素都是独一无二的。
1 <= target <= 500
```

## 代码
### 自己写的版本
这一版我自己写的利用回溯法，本地测试用例都AC了，但是在提交的时候显示我[1],2这一测试用例输出的结果为[]，但是我在本机测试的结果却是正确的。

![figure.1](https://gitee.com/zyp521/upload_image/raw/master/FD2nfl.png)

![figure.2](https://gitee.com/zyp521/upload_image/raw/master/zVWnkh.png)

没想明白裂开。  


```
class Solution(object):
    sort_result = []
    def backtrack(self, target, candidates, temp):
        if sum(temp) == target:
            result.append(temp)
            self.sort_result.append(sorted(temp))
            #print(temp)
            return self.backtrack(target,candidates,[]),result
        if target < sum(temp):
            return False
        for i in range(len(candidates)):
            temp.append(candidates[i])
            if sorted(temp) in self.sort_result:
                temp.pop()
                continue
            if self.backtrack(target,candidates,temp):
                return True
            temp.pop()
                
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        核心思想：
                分析题目同样可以看出我们应该使用回溯法进行求解
        回溯法的标准框架
        def backtrack(path, selected):
            if 满足停止条件：
                res.append(path)
            for 选择 in 选择列表：
                做出选择
                递归执行backtrack
                    满足则return True
                如果不满足要求就撤销选择
        """
        global result
        result = []
        self.backtrack(target,candidates,[])
        #print(result)
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum(candidates = [1], target = 2))

```

## AC的版本
```
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        def backtrack(i, tmp_sum, tmp):
            if  tmp_sum > target or i == n:
                return 
            if tmp_sum == target:
                res.append(tmp)
                return 
            for j in range(i, n):
                if tmp_sum + candidates[j] > target:
                    break
                backtrack(j,tmp_sum + candidates[j],tmp+[candidates[j]])
        backtrack(0, 0, [])
        return res
```