---
title: LeetCode No.89

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第八十九题—格雷编码
## 题目描述
格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。

给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。即使有多个不同答案，你也只需要返回其中一种。

格雷编码序列必须以 0 开头。

```

示例 1:

输入: 2
输出: [0,1,3,2]
解释:
00 - 0
01 - 1
11 - 3
10 - 2

对于给定的 n，其格雷编码序列并不唯一。
例如，[0,2,3,1] 也是一个有效的格雷编码序列。

00 - 0
10 - 2
11 - 3
01 - 1
示例 2:

输入: 0
输出: [0]
解释: 我们定义格雷编码序列必须以 0 开头。
     给定编码总位数为 n 的格雷编码序列，其长度为 2n。当 n = 0 时，长度为 20 = 1。
     因此，当 n = 0 时，其格雷编码序列为 [0]。
```

## 代码
```
class Solution(object):
    def TimeOut(self, n):
        """
        :type n: int
        :rtype: List[int]

        核心思想：
                考虑用回溯法来做吧，题解里面提到的镜像操作，说实话我是真想不到塞
                 def backtrack(path, selected):
                    if 满足停止条件：
                        res.append(path)
                    for 选择 in 选择列表：
                        做出选择
                        递归执行backtrack
                            满足则return True
                        如果不满足要求就撤销选择
                注意使用 << 是位运算
                cur = 1 << i ^ res[-1] 表示将结果list中最后一个进行位移操作
        """
        res = [0] # 使用list存储  初始一个0针对0的情况
        def backtrack(cur): # cur当前生成的元素
            # 停止条件
            if len(res) == 2**n:
                return res
            for i in range(n):
                # 做出选择
                cur = 1 << i ^ res[-1] # 移位运算
                if cur in res:
                    continue
                res.append(cur)
                temp = backtrack(cur)
                if temp:
                    return temp
                # 撤销选择
                res.pop()
        return backtrack(res[0])
    def grayCode(self,n):
        """
            :type n: int
            :rtype: List[int]

            回溯法成功超时试了，去看了一下评论区大佬的解答

            找到了一个核心的思想：自己与自己左移一位进行异或，得到的就是它的格雷码
        """
        res = []
        for i in range( 1<<n ):
            res.append(i ^ i >> 1)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.grayCode(n=2))
```