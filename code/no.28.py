class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == "" and needle == "":
            return 0
        index = -1
        for i in range(len(haystack)):
            if i + len(needle) > len(haystack):
                break
            if haystack[i:i+len(needle)] == needle:
                index = i
                break
        return index

if __name__ == '__main__':
    s = Solution()
    print(s.strStr(haystack = "hello", needle = "ll"))