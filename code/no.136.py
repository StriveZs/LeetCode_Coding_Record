class Solution(object):
    def singleNumber(self, nums):
        """
        考虑用字典存储就好了
        :type nums: List[int]
        :rtype: int
        """
        res_dict = dict()
        min_index = -1
        min_count = 10000
        for i in range(len(nums)):
            if nums[i] not in res_dict.keys():
                res_dict[nums[i]] = 1
            else:
                res_dict[nums[i]] += 1
        res_dict = dict(sorted(res_dict.items(), key=lambda item:item[1]))
        return list(res_dict.keys())[0]

    def faster_OR(self, nums):
        """
        参考大佬们的想法，采用异或操作: 还是要结合题意的，只有一个元素出现一次，其他元素出现两次，按照异或的规则，是可以进行操作的，如果其他的元素出现任意次，则不行
            异或满足:
                1.交换律：a ^ b ^ c <=> a ^ c ^ b
                2.任何数于0异或为任何数 0 ^ n => n
                3.相同的数异或为0: n ^ n => 0
            因此可以考虑如下:
            比如a = [2,3,3,3,4,4,2,1]
            2^3^3^4^4^2^1 = 2^2^3^3^3^4^4^4^1 = 0^3^3^4^4^4^1 = 3^3^4^4^1 = 0^4^4^1 = 4^4^1 = 0^1 = 1
        :param num:
        :return:
        """
        res = nums[0]
        for i in range(1, len(nums)):
            res = res ^ nums[i]
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.faster_OR([1,4,2,1,2]))