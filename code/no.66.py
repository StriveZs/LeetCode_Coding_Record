class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]

        核心思想：
                就是将数字转换为对应的数字，然后加1，再将其转换为列表
                剪枝：对于尾数不为9的情况，直接在尾数加1返回即可
                    如果为9的话，则再转换为数字后加1再逆变换集合

                另外还有一种思想：在原数组上直接考虑进位即可，如果9+1的话原位等0，进1如果前一位不为9则直接上即可
                            如果为9则重复上述直到加到最高位的话，则直接在结果前插入1即可。
        """
        if digits[-1] != 9:
            digits[-1] = digits[-1] + 1
            return digits
        str1 = ''
        for i in range(len(digits)):
            str1 += str(digits[i])
        temp = str(int(str1) + 1)
        result = []
        for i in range(len(temp)):
            result.append(int(temp[i]))
        return result
    def otherMethod(self,digits):
        i = len(digits)-1
        while digits[i] == 9:
            digits[i] = 0
            i -= 1
        if i == -1:
            digits = [1] + digits
        else:
            digits[i] += 1
        return digits

if __name__ == '__main__':
    s = Solution()
    print(s.otherMethod([6,9,6,9]))