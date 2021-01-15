class Solution(object):
    # 判断是否为数字
    def isNum(self,s):
        if s == '0' or s == '1' or s == '2' or s == '3' or s == '4' or s == '5' or \
        s == '6' or s == '7' or s == '8' or s == '9':
            return True
        else:
            return False

    # 丢弃开头空白字符
    def deleteKong(self,s):
        index = 0
        for i in range(len(s)):
            if s[i] != ' ':
                index = i
                break
        s = s[index:]
        return s

    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = self.deleteKong(s)
        flag = False # 正负标志
        if len(s) == 0:
            return 0
        if len(s) == 1 and s[0] == '-':
            return 0
        if len(s) == 1 and s[0] == '+':
            return 0
        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                flag = True
            else:
                flag = False
            s = s[1:]
        if self.isNum(s[0]):
            result = ''
            for i in range(len(s)):
                if self.isNum(s[i]):
                    result += s[i]
                else:
                    break
            result = int(result)
            if result < -(2**31) or result > (2**31)-1:
                if flag:
                    return -(2**31)
                else:
                    return (2**31)-1
            else:
                if flag:
                    return -1*result
                else:
                    return result
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi('2147483648'))