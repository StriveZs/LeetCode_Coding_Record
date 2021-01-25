class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        string = list(s)
        stack = []
        flag = True
        for s in string:
            if s == '(' or s == '[' or s == '{':
                stack.append(s)
            elif s == ')':
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if temp != '(':
                    return False
            elif s == ']':
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if temp != '[':
                    return False
            elif s == '}':
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if temp != '{':
                    return False
        if len(stack) != 0:
            return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isValid("{{{{"))


