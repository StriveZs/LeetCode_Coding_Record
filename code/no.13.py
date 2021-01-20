class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictList = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']  # 特殊规则字符
        numList = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]  # 特殊规则数字

        dicts = zip(dictList,numList)
        dicts = dict(dicts)
        dictSet = set(dictList)
        result = 0
        i = len(s) - 1
        while i >= 0:
            if i == 0:
                result += dicts[s[i]]
                i -= 1
            else:
                if s[i] == 'V' or s[i] == 'X':
                    if s[i - 1] == 'I':
                        temp = s[i - 1] + s[i]
                        result += dicts[temp]
                        i -= 2
                    else:
                        result += dicts[s[i]]
                        i -= 1
                elif s[i] == 'L' or s[i] == 'C':
                    if s[i - 1] == 'X':
                        temp = s[i - 1] + s[i]
                        result += dicts[temp]
                        i -= 2
                    else:
                        result += dicts[s[i]]
                        i -= 1
                elif s[i] == 'D' or s[i] == 'M':
                    if s[i - 1] == 'C':
                        temp = s[i - 1] + s[i]
                        result += dicts[temp]
                        i -= 2
                    else:
                        result += dicts[s[i]]
                        i -= 1
                else:
                    result += dicts[s[i]]
                    i -= 1
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('CX'))