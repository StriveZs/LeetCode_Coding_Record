---
title: LeetCode No.134

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第134题—加油站

自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。

说明: 

- 如果题目有解，该答案即为唯一答案。
- 输入数组均为非空数组，且长度相同。
- 输入数组中的元素均为非负数。
```
示例 1:

输入: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

输出: 3

解释:
从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可为起始索引。
示例 2:

输入: 
gas  = [2,3,4]
cost = [3,4,3]

输出: -1

解释:
你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
因此，无论怎样，你都不可能绕环路行驶一周。
```
## 代码
```
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        分析：
            第i个加油站有gas[i]升汽油，从第i个加油站开往第i+1个加油站需要消耗汽油cost[i]升，从这里可以看出，行驶方向只能正序0->1->2这种
            油箱容量无限，从其中一个加油站出发，初始油箱为空
            目标：绕环路一圈，则返回出发加油站编号，否则返回-1  (如果有解则解唯一)
        思路:
            1. 用gas对应位去减去cost得到一个subtraction
            2. subtraction的总和大于等于0的话，则一定是有解的
            3. 如果有解的话，subtraction为负值的地方，则表示不能作为初始的位置, 所有非负的地方都可以作为候选起始位置，这个时候要要根据subtraction来判断那个位置作为初始位置(唯一)
            4. 依次判断上面非负位置
            5. 可能会出现几种结束条件
              i) i=0 j=4 总和满足大于等于0的合法情况
              ii) i=3 j=2 总和满足大于等于0的合法情况
              iii) 总和小于0的非法情况
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        subtraction = list(map(lambda x:x[0]-x[1],zip(gas,cost))) # 进行数组对应位相减
        for i in range(len(subtraction)):
            if subtraction[i] < 0:
                continue
            j = i
            curSum = 0
            while True:
                curSum += subtraction[j]
                # i=4 j=3这种情况的结束条件
                if j == i-1:
                    break
                # j=4 i=0这种情况的结束条件
                if j - i + 1 == len(subtraction):
                    break
                if curSum < 0:
                    break
                if j < len(subtraction)-1:
                    j += 1
                else:
                    j = 0
            # 符合的判决条件
            if (j == i-1 or j - i + 1 == len(subtraction)) and curSum >=0 :
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.canCompleteCircuit([3,1,1],[1,2,2]))

```