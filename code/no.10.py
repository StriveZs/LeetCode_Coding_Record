import re

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        matchObject = re.match(p,s)
        # print(result)
        if matchObject:
            if matchObject.group() == s:
                return True
            else:
                return False
        else:
            return False
    
if __name__ == '__main__':
    s = Solution()
    print(s.isMatch('ab','.c'))