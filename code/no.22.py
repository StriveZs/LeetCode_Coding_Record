class Solution(object):
    def func(self,strlist, string, l, r, n):
        # 单边递归结束条件
        if l > n or r > n or r > l:
            return

        # string生成结束条件
        if l == n and r == n:
            strlist.append(string)
            return
        self.func(strlist, string + '(', l+1, r, n)
        self.func(strlist, string + ')', l, r+1, n)
        return


    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        strlist = []
        self.func(strlist, "", 0, 0, n)
        return strlist

if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
