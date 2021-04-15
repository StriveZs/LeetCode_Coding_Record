---
title: LeetCode No.84

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第八十四题—柱状图中的最大的矩形
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

![figure.1](https://gitee.com/zyp521/upload_image/raw/master/jn1rXo.jpg)

以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

![figure.2](https://gitee.com/zyp521/upload_image/raw/master/CpZgks.jpg)
```
示例:

输入: [2,1,5,6,2,3]
输出: 10
```
## 分析

```
例子分析：要保证栈为单调增栈
    对于[2,1,5,6,2,3,0] 输入
    stack:2  因为1 < 2 因此计算2 得到面积为2  2出栈 1入栈
    stack:1 因为5>1 所以5入栈
    stack:1 5 因为6>5 所以6入栈
    stack:1 5 6 因为 2<6 因此计算6(栈顶) 得到面积6  6出栈 又因为 2<5 因此接着计算5(当前栈顶) 得到面积10 5出栈  2入栈
    stack:1 2 因为2>3 所以3入栈
    stack:1 2 3 访问结束，依次计算3 2 1 这里可以在高度柱表中引入一个0
```
计算图表:

![figure.0](https://gitee.com/zyp521/upload_image/raw/master/ZzLRmf.jpg)

## 代码
```
class Solution(object):
    def TimeOut(self, heights):
        """
        :type heights: List[int]
        :rtype: int

        感觉有点类似水桶漏水那道题
        核心思想：
                暴力法，依次遍历每个柱子，然后依次找它两边比它短的柱子，并累加面积即可
                注意特别处理最两边的柱子
                如果当前柱子的大小比前一个柱子大，则在上一个柱子面积上累加，只需要往后找比当前柱子长度大于等于的相邻柱子即可
        """
        maxInt = 0
        for i in range(len(heights)):
            if heights[i] == 0:
                continue
            num = 0 # 计数菌 大于等于当前柱子值的柱子数目，如果存在比当前柱子数目小的柱子 则结束统计
            for j in range(i+1,len(heights)):
               if heights[j] > heights[i]:
                   num += 1
               else:
                   break
            if i == 0:
                maxInt = max(maxInt,(num+1) * heights[i])
            elif heights[i - 1] < heights[i]:
                maxInt = max(maxInt,num * heights[i] + heights[i])
            else:
                pre = i
                for j in range(0,i+1):
                    if heights[i-j] < heights[i]:
                        break
                    pre = i-j
                maxInt = max(maxInt,(i-pre)*heights[i] + num*heights[i] + heights[i])
        return maxInt
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int

        上一个暴力解法成功超时了，下面是参考带佬写的单调栈来求解，看评论JAVA版本的暴力解法是可以通过，Python党震怒
        思路：
            对于一个高度，如果能得到向左和向右的边界
            那么就能对每个高度求一次面积
            遍历所有高度，即可得出最大面积
            使用单调栈，在出栈操作时得到前后边界并计算面积
        单调栈介绍:
        1.单调栈分为单调递增栈和单调递减栈
            11. 单调递增栈即栈内元素保持单调递增的栈
            12. 同理单调递减栈即栈内元素保持单调递减的栈

        2.操作规则（下面都以单调递增栈为例）
            21. 如果新的元素比栈顶元素大，就入栈
            22. 如果新的元素较小，那就一直把栈内元素弹出来，直到栈顶比新元素小

        3.加入这样一个规则之后，会有什么效果
            31. 栈内的元素是递增的
            32. 当元素出栈时，说明这个新元素是出栈元素向后找第一个比其小的元素
        """
        maxInt = 0 # 最大值
        stack = [] # 单调增栈
        heights.insert(0,0) # 首尾＋一个0  防止下面right left超出边界
        heights.append(0)
        # 计算方式不是顺序计算，是先从最大的柱开始计算，依次计算小的柱
        for i in range(len(heights)):
            while len(stack) != 0 and heights[stack[len(stack)-1]] > heights[i]:
                # 找到了比当前栈顶小的元素 则结束开始计算当前栈顶对应的面积
                cur = stack[len(stack)-1]
                stack.pop()
                left = stack[len(stack)-1] + 1
                right = i - 1
                maxInt = max(maxInt,(right-left+1) * heights[cur])
            stack.append(i)
        return maxInt

if __name__ == '__main__':
    s = Solution()
    print(s.largestRectangleArea([2,1,5,6,2,3]))
```