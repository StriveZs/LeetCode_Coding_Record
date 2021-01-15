---
title: LeetCode No.7

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第七题
今天晚上看了会直播，所以来晚了，一般不缺勤呢。过几天反向跑毒完，我回家还要坚持背英语。  

## 题目描述
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

 

注意：

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
 
```
示例 1：

输入：x = 123
输出：321
示例 2：

输入：x = -123
输出：-321
示例 3：

输入：x = 120
输出：21
示例 4：

输入：x = 0
输出：0
 

提示：

-231 <= x <= 231 - 1
```

## 代码
### Python版本
```
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = False

        if x == 0:
            return x
        if x < 0:
            flag = True
            x = abs(x)
        item = list(str(x))
        item_reverse = item[::-1]
        result = ''
        for i in range(len(item_reverse)):
            result += item_reverse[i]
        result = int(result)
        if flag:
            result = -1 * result
        if result < -(2**31) or result > (2**31):
            return 0
        return result

if __name__ == '__main__':
    s = Solution()
    print(2**31)
    print(s.reverse(1534236469))

```


### C++版本
```
#include <string.h>
#include <algorithm>
#include <math.h>
class Solution {
public:
    int reverse(int x) {
        int result = 0;
        int pop = 0;
        while(x != 0){
            pop = x % 10; //取出最右变得数字
            x /= 10; //实际上就是完成了 从 123 变成 12 并且取出 3 
            if(result > INT_MAX / 10 || (result == INT_MAX / 10 && pop > 7)){//判断上限
                return 0;
            }
            if(result < INT_MIN / 10 || (result == INT_MIN / 10 && pop < -8)){//判断下限
                return 0;
            }
            result = result * 10 + pop;
        }
        return result;
    }
};
```