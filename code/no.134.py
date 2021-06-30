class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        分析：
            第i个加油站有gas[i]升汽油，从第i个加油站开往第i+1个加油站需要消耗汽油cost[i]升，从这里可以看出，行驶方向只能正序0->1->2这种
            油箱容量无限，从其中一个加油站出发，初始油箱为空
            目标：绕环路一圈，则返回出发加油站编号，否则返回-1  (如果有解则解唯一)
        思路:
            1. 用gas对应位去减去cost得到一个subtraction
            2. subtraction的总和大于等于0的话，则一定是有解的
            3. 如果有解的话，subtraction为负值的地方，则表示不能作为初始的位置, 所有非负的地方都可以作为候选起始位置，这个时候要要根据subtraction来判断那个位置作为初始位置(唯一)
            4. 依次判断上面非负位置
            5. 可能会出现几种结束条件
              i) i=0 j=4 总和满足大于等于0的合法情况
              ii) i=3 j=2 总和满足大于等于0的合法情况
              iii) 总和小于0的非法情况
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        subtraction = list(map(lambda x:x[0]-x[1],zip(gas,cost))) # 进行数组对应位相减 (这一步也耗时，后续改进的话，可以将它放在需要用到的位置再进行相减)
        for i in range(len(subtraction)):
            if subtraction[i] < 0:
                continue
            j = i
            curSum = 0
            while True:
                curSum += subtraction[j]
                # i=4 j=3这种情况的结束条件
                if j == i-1:
                    break
                # j=4 i=0这种情况的结束条件
                if j - i + 1 == len(subtraction):
                    break
                if curSum < 0:
                    break
                if j < len(subtraction)-1:
                    j += 1
                else:
                    j = 0
            # 符合的判决条件
            if (j == i-1 or j - i + 1 == len(subtraction)) and curSum >=0 :
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.canCompleteCircuit([3,1,1],[1,2,2]))
