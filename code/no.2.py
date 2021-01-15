class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l1 = [l1[len(l1)-i-1] for i in range(len(l1))]
        str1 = ""
        for i in range(len(l1)):
            str1 = str1 + str(l1[i])
        # print(int(str1))
        l2 = [l2[len(l2) - i - 1] for i in range(len(l2))]
        str2 = ""
        for i in range(len(l2)):
            str2 = str2 + str(l2[i])
        # print(int(str1))
        result = list(str(int(str1) + int(str2)))
        result_list = []
        #print(result)
        for i in range(len(result)):
            result_list.append(int(result[len(result) - i - 1]))
        #print(result_list)
        return result_list


if __name__ == '__main__':
    s = Solution()
    s.addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9])