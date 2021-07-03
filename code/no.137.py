class Solution(object):
    def singleNumber(self, nums):
        """
        还是考虑使用以前的异或操作，这里建立一个记忆字典，如果一个数出现了3次，则本次异或运算该数不参与运算了
        所有的数只能出现3次或者1次，而且只有一个数可以出现1次 (充分利用这个思想)
        然后就可以按照上一题的思路来做了:
        异或^:
            n ^ n = 0
            0 ^ n = n
        :type nums: List[int]
        :rtype: int
        """
        memory = dict()
        res = nums[0]
        memory[res] = 1 # 出现次数设为1
        for i in range(1, len(nums)):
            if nums[i] not in memory.keys():
                memory[nums[i]] = 1
            else:
                memory[nums[i]] += 1
            # 出现第三次就跳过
            if memory[nums[i]] == 3:
                continue

            res = res ^ nums[i]
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([2,2,3,2]))