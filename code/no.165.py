#
# @lc app=leetcode.cn id=165 lang=python
#
# [165] 比较版本号
#

# @lc code=start
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        用split划分 转换为int 比较即可
        :type version1: str
        :type version2: str
        :rtype: int
        """
        com1 = version1.split('.')
        com2 = version2.split('.')
        # 排除特殊情况
        if len(com1) != len(com2):
            # 单独处理 1.0 1.0.0的情况
            if len(com1) > len(com2):
                for i in range(len(com2)):
                    if int(com1[i]) > int(com2[i]):
                        return 1
                    elif int(com1[i]) < int(com2[i]):
                        return -1
                for i in range(len(com2), len(com1)):
                    if int(com1[i]) != 0:
                        return 1
                return 0
            else:
                for i in range(len(com1)):
                    if int(com1[i]) > int(com2[i]):
                        return 1
                    elif int(com1[i]) < int(com2[i]):
                        return -1
                for i in range(len(com1), len(com2)):
                    if int(com2[i]) != 0:
                        return -1
                return 0

        # 长度相同的情况
        for i in range(len(com1)):
            if int(com1[i]) > int(com2[i]):
                return 1
            elif int(com1[i]) < int(com2[i]):
                return -1
            else:
                continue
        return 0
# @lc code=end
