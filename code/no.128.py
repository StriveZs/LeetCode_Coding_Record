class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        核心思想:
            考虑用字典存储当前长度
            dict[a] = b 表示这个每个端点值对应连续区间的长度
            键值是顺序从小到大的
        """
        max_length = 0
        res_dict = dict()
        for num in nums:
            # 去掉重复情况
            if num not in res_dict.keys():
                # 找到它的左端值和右端值
                left_length = res_dict.get(num-1,0) # 如果左边值存在则和左边值连续，否则返回0
                right_length = res_dict.get(num+1,0) # 如果右边值存在，则和右边值连续，否则返回0
                length = left_length + right_length + 1
                if length > max_length:
                    max_length = length
                # 更新字典值
                res_dict[num] = length
                # 更新左邻域最大长度(没有的话不更新)
                res_dict[num-left_length] = length
                # 更新有邻域最大长度(如果没有的话，则不更新)
                res_dict[num+right_length] = length
        return max_length
