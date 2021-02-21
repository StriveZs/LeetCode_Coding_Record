class Solution(object):
    # 大数加法
    def addPly(self,num1,num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        核心思想：经典的大数加法
                核心就是循环 每次分别计算进位和计算余位，注意整数和字符串的转换
        """
        num1_reverse = num1[::-1]
        num2_reverse = num2[::-1]
        result = [str(0) for i in range(1000)]
        # 将一个值赋给result
        for i in range(len(num1_reverse)):
            result[i] = num1_reverse[i]
        # 将另外一个值加到result上
        temp = 0
        for i in range(len(num2_reverse)):
            temp += (int(result[i]) + int(num2_reverse[i]))
            result[i] = str(temp % 10)
            temp = int(temp / 10)
        result[len(num2_reverse)] = str(int(result[len(num2_reverse)]) + temp)
        result = result[::-1]
        str_res = ""
        flag = True
        for i in range(len(result)):
            if flag:
                if result[i] != '0':
                    flag = False
                    str_res += result[i]
            else:
                str_res += result[i]
        # 单独处理为0的情况
        if flag:
            return "0"
        return str_res

    # 找到两个数中更大的一个数，判断正负号
    def getBiggerOne(self,num1,num2):
        if len(num1) > len(num2):
            return False
        elif len(num1) < len(num2):
            return True
        else:
            for i in range(len(num1)):
                if num1[i] != num2[i]:
                    if int(num1) > int(num2):
                        return False
                    else:
                        return True

    # 大数减法
    def subtractPly(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        核心思想：经典的大数减法
                核心就是循环 每次分别计算借位和计算余位，注意要保证大数减小数
        """
        # 保证num1 大于 num2
        if num1 == num2:
            return "0"
        flag = self.getBiggerOne(num1,num2)
        if flag:
            temp = num2
            num2 = num1
            num1 = temp
        num1_reverse = num1[::-1]
        num2_reverse = num2[::-1]
        result = [str(0) for i in range(10)]
        for i in range(len(num1)):
            result[i] = num1_reverse[i]
        for i in range(len(num2)):
            temp1 = int(result[i])
            temp2 = int(num2_reverse[i])
            if temp1 >= temp2:
                result[i] = str(temp1 - temp2)
            else:
                # 借位 由于事先保证了num1大于num2 则借位不会出现为负的情况
                result[i+1] = str(int(result[i+1]) - 1)
                result[i] = str(int(result[i]) + 10 - int(num2_reverse[i]))
        result = result[::-1]
        #print(result)
        str_res = ""
        flag1 = True
        for i in range(len(result)):
            if flag1:
                if result[i] != '0':
                    flag1 = False
                    str_res += result[i]
            else:
                str_res += result[i]
        if flag:
            str_res = '-' + str_res
        return str_res

    # 大数乘法
    def multiPly(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        核心思想：经典的大数乘法
                核心就是循环 每次分别计算进位和计算余位，注意整数和字符串的转换
        """
        num1_reverse = num1[::-1]
        num2_reverse = num2[::-1]
        result = [str(0) for i in range(1000)]
        for i in range(len(num1_reverse)):
            for j in range(len(num2_reverse)):
                temp = int(num1_reverse[i]) * int(num2_reverse[j])
                # 计算进位
                result[i+j+1] = str(int(result[i+j+1]) + int((int(result[i+j]) + temp) / 10))
                # 计算余位
                result[i+j] = str((int(result[i+j]) + temp) % 10)

        result = result[::-1]
        #print(result)
        str_res = ""
        flag = True
        for i in range(len(result)):
            if flag:
                if result[i] != '0':
                    flag = False
                    str_res += result[i]
            else:
                str_res += result[i]
        # 单独处理为0的情况
        if flag:
            return "0"
        return str_res

    # 大数除法
    def divisionPly(self,num1,num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        核心思想：经典的大数除法
                实质上就是大数减法的叠加
        """
        result = [str(0) for i in range(1000)]
        # 如果num1小于num2，则num1/num2的商为0
        if self.getBiggerOne(num1,num2):
            return "0"
        length1 = len(num1)
        length2 = len(num2)
        disc = length1 - length2 # 记录除数和被除数之间位数之差 扩大除数disc个0
        for i in range(disc):
            num2 += '0' # 补0

        # 利用大数减法进行除法操作
        while disc >= 0:
            sum = 0 # 用减法来代替除法，计算减了多少次
            temp = self.subtractPly(num1,num2)
            while True:
                if temp[0] == '-':
                    break
                sum += 1
                num1 = temp
                temp = self.subtractPly(num1,num2)
            result[len(result)-disc-1] = str(sum)  # 将减的次数加上去
            disc -= 1
            num2 = num2[0:length2+disc]
        str_res = ""
        flag = True
        for i in range(len(result)):
            if flag:
                if result[i] != '0':
                    flag = False
                    str_res += result[i]
            else:
                str_res += result[i]
        return str_res



if __name__ == '__main__':
    s = Solution()
    print(s.divisionPly('122','2'))