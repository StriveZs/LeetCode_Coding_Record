class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]

        核心思想:
                回溯算法
                def backtrack(path, selected):
                    if 满足停止条件：
                        res.append(path)
                    for 选择 in 选择列表：
                        做出选择
                        递归执行backtrack
                            满足则return True
                        如果不满足要求就撤销选择
                满足条件判断：
                    1. 位于0-255之间
                    2. 以0开头的不满足，比如：01 02 010等
                    3. 含有非法字符不满足
                    4. 划分部分必须等于4部分
                存储结构使用[]存储，将满足的[]在存到result中
        """
        self.res = []
        # 去除长度大于12的情况，因此长度大于12，属于非法的
        if len(s) > 12:
            return self.res
        # 回溯
        def backtrack(s, path):
            if len(path) == 4:
                if path not in self.res:
                    self.res.append('.'.join(path))
                    return
            # 已经选择了3个
            if len(path) == 3 and s != '':
                temp = s
                # 选择合法的情况
                if int(temp) >= 0 and int(temp) <= 255:
                    # 去除前导为0的情况，如果前导存在0，则不再进行递归
                    if str(int(temp)) == temp:
                        backtrack('',path+[temp])
            # 选择一个1或者两个或者0个的情况都是一样的
            elif len(path) < 3 and s != '':
                # 最大可选择的长度为3
                if len(s) <= 3:
                    for i in range(len(s)):
                        temp = s[:i+1]
                        next = s[i+1:]
                        if int(temp) >= 0 and int(temp) <= 255:
                            # 去除前导为0的情况，如果前导存在0，则不再进行递归
                            if str(int(temp)) == temp:
                                backtrack(next, path+[temp])
                else:
                    for i in range(3):
                        temp = s[:i + 1]
                        next = s[i + 1:]
                        if int(temp) >= 0 and int(temp) <= 255:
                            # 去除前导为0的情况，如果前导存在0，则不再进行递归
                            if str(int(temp)) == temp:
                                backtrack(next, path+[temp])
        backtrack(s, [])
        return self.res
                        
if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses("1111"))