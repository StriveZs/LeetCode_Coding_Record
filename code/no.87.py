class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool

        核心思想:
                感觉就是暴力搜索
                这里采用递归搜索
        """
        n = len(s1)
        if n == 1:
            return s1 == s2
        # 递归搜索所有可能
        for i in range(1,n):
            # 分别对划分两部分进行递归搜索
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
                return True
            # 交换匹配 比如：acb 和 bac 中ac和ac 匹配 b和b 这种情况 也可以是a和c cb和ba
            elif self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:],s2[:-i]):
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.isScramble("abcdefghijklmnopq","efghijklmnopqcadb"))