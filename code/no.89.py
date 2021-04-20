class Solution(object):
    def TimeOut(self, n):
        """
        :type n: int
        :rtype: List[int]

        核心思想：
                考虑用回溯法来做吧，题解里面提到的镜像操作，说实话我是真想不到塞
                 def backtrack(path, selected):
                    if 满足停止条件：
                        res.append(path)
                    for 选择 in 选择列表：
                        做出选择
                        递归执行backtrack
                            满足则return True
                        如果不满足要求就撤销选择
                注意使用 << 是位运算
                cur = 1 << i ^ res[-1] 表示将结果list中最后一个进行位移操作
        """
        res = [0] # 使用list存储  初始一个0针对0的情况
        def backtrack(cur): # cur当前生成的元素
            # 停止条件
            if len(res) == 2**n:
                return res
            for i in range(n):
                # 做出选择
                cur = 1 << i ^ res[-1] # 移位运算
                if cur in res:
                    continue
                res.append(cur)
                temp = backtrack(cur)
                if temp:
                    return temp
                # 撤销选择
                res.pop()
        return backtrack(res[0])
    def grayCode(self,n):
        """
            :type n: int
            :rtype: List[int]

            回溯法成功超时试了，去看了一下评论区大佬的解答

            找到了一个核心的思想：自己与自己左移一位进行异或，得到的就是它的格雷码
        """
        res = []
        for i in range( 1<<n ):
            res.append(i ^ i >> 1)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.grayCode(n=2))