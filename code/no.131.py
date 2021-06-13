import copy
class Solution(object):
    res = []
    # fixme:判断是否是回文串
    def isPalindrome(self, s):
        if s == s[::-1]:
            return True
        return False

    def partition(self, s):
        """
        最终的结果，每个字符单独拿出来肯定是一个回文串, 因此不存在空字符串结果的情况，除非输入就是空串
        算法考虑的话，有两种方法:
            1. 动态规划
            2. 回溯法
        :type s: str
        :rtype: List[List[str]]
        """
        self.res = []
        # 回溯法
        def backtrack(s, path):
            if len(s) == 0:
                tt = copy.copy(path) # 如果直接用self.res.append(path)的话，由于是浅拷贝，后面再path.remove的话，res中的结果也会被修改
                self.res.append(tt)
            for i in range(1, len(s) + 1):  # 注意起始和结束位置
                if self.isPalindrome(s[:i]):
                    path.append(s[:i])
                    backtrack(s[i:], path)
                    path.remove(s[:i])
        backtrack(s,[])
        return self.res

if __name__ == '__main__':
    s = Solution()
    print(s.partition("a"))