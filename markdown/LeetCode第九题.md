---
title: LeetCode No.9

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第九题
今天从天津回石家庄，跑了一天晚上才收拾好，今天就做了个简单的题目，明天争取两道题，干巴爹。  

## 题目描述
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
```
示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:
```
你能不将整数转为字符串来解决这个问题吗？  

## 代码
### Python版本
```
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x = str(abs(x))
        reverse_x = x[::-1]
        if reverse_x == x:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(10))
```

### C++版本
```
class Solution {
public:
    string intToStr(int number){
        string result = "";
        bool flag = false;
        int temp = number;
        while(temp != 0){
            result += ((temp % 10) + '0');
            temp /= 10;
        }
        reverse(result.begin(),result.end());
        return result;
    }
    bool isPalindrome(int x) {
        if(x < 0){
            return false;
        }
        else{
            string goal="";
            string use = goal = intToStr(x);
            reverse(use.begin(),use.end());
            if(use == goal){
                return true;
            }
            else{
                return false;
            }
        } 
    }
};

```