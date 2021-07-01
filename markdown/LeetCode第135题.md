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


# LeetCode第135题—分发糖果
今天是建党100周年，祝愿祖国繁荣富强！

自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

你需要按照以下要求，帮助老师给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
评分更高的孩子必须比他两侧的邻位孩子获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？

```
示例 1：

输入：[1,0,2]
输出：5
解释：你可以分别给这三个孩子分发 2、1、2 颗糖果。
示例 2：

输入：[1,2,2]
输出：4
解释：你可以分别给这三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这已满足上述两个条件。
```

## 代码
```
class Solution(object):
    def candy(self, ratings):
        """
        题目分析:
            N个孩子站成一条直线，每个孩子的评分提前给出
            分配规则:
            1.每个孩子至少分配到一个糖果
            2.评分更高的孩子必须比他两侧的相邻的孩子获得更多地糖果, 但是如果这个孩子和旁边孩子分数相同，则它可以为1
            3.如果一个孩子比他旁边的一个孩子分低，则只需要保证他分配的糖果比这个孩子少就行，同时保证比他另一个分低的孩子糖果多

            相邻分配情况:
            1. 分数相同: 1
            2. 分数为3 1 2: 中间分配1个
            3. 分数为3 2 1: 中间分配2个
            4. 分数为1 3 2: 中间分配3个

            需求:老师至少需要多少个糖果?
        解题思路:
            必然是秉持着贪心的思想来进行分配的，最小化分配的原则，默认初始所有人分配1个
            分两个方向进行遍历，不要同时兼顾左边和右边，否则会顾此失彼
            ① 正序遍历，先处理中间孩子和前面一个孩子进行比较
            ② 倒序遍历，再处理中间孩子和后面一个孩子进行比较
            如果中间孩子大于前面孩子则他的基础上+1，同理中间孩子如果大于后面孩子则他的基础上+1
            其他小于等于均不作处理
            在糖果个数本来就大的情况下，就不需要再加了
        (还有一种暴力的方法，就是先处理分数最低的孩子，然后依次处理分数高得孩子，有点类似于对位处理，但是估计会超时)
        :type ratings: List[int]
        :rtype: int
        """
        candies = [1] * len(ratings)
        # 正序遍历
        for i in range(1,len(ratings)):
            # 在糖果个数本来就大的情况下，就不需要再加了
            if ratings[i] > ratings[i-1] and candies[i] <= candies[i-1]:
                candies[i] = candies[i-1] + 1

        # 倒序遍历
        for i in range(1, len(ratings)):
            # # 在糖果个数本来就大的情况下，就不需要再加了
            if ratings[len(ratings) - i] < ratings[len(ratings) - i - 1] and candies[len(ratings) - i] >= candies[len(ratings) - i - 1]:
                candies[len(ratings) - i - 1] = candies[len(ratings) - i] + 1
        #print(candies)
        return sum(candies)

if __name__ == '__main__':
    s = Solution()
    print(s.candy([1,0,2]))
```