class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str

        核心思想：
            几点约束：
                1.一个点（.）表示当前目录本身；
                2.两个点 （..） 表示将目录切换到上一级（指向父目录）；
                3.两者都可以是复杂相对路径的组成部分。
                3.任意多个连续的斜杠（即，'//'）都被视为单个斜杠 '/' 。
                4.对于此问题，任何其他格式的点（例如，'...'）均被视为文件/目录名称。
            返回路径的要求：
                1. 始终以斜杠 '/' 开头。
                2.两个目录名之间必须只有一个斜杠 '/' 。
                3.最后一个目录名（如果存在）不能 以 '/' 结尾。
                4.路径仅包含从根目录到目标文件或目录的路径上的目录（即，不含 '.' 或 '..'）

            可以考虑使用栈来操作，从后往前算
        """
        input = path.split('/')
        stack = []
        dotList = ['.','..','']  # ''针对的是//被划分出来的结果''
        for i in range(len(input)):
            if input[i] not in dotList:
                stack.append(input[i])
            else:
                if input[i] == '..': # 返回上一级
                    if len(stack) != 0:
                        stack.pop()
        res = ''
        if len(stack) == 0:
            return '/'
        for i in range(len(stack)):
            res = res + '/' + stack[i]
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.simplifyPath("/home/"))
