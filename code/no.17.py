import itertools

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        # 字典查表
        numList = ['2','3','4','5','6','7','8','9']
        characterList = [['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        temp = zip(numList,characterList)
        dictList = dict(temp)
        #print(dictList)

        digitsList = list(digits)
        numCharaList = []
        sumRes = 1
        # 统计输入的数字对应的字母
        for i in range(len(digitsList)):
            numCharaList.append(dictList[digitsList[i]])
        #print(numCharaList)

        # 生成结果
        result = []
        temp = list(itertools.product(*numCharaList))  # 调用库来生成列表排列组合
        for i in range(len(temp)):
            str1 = ''
            for j in range(len(list(temp[i]))):
                str1 += temp[i][j]
            result.append(str1)
        return result



if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('23'))