class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    depth_dict = dict() # 深度字典
    # fixme:采用bfs添加深度，将相同的深度放在同一个列表中
    def bfs(self, node, depth):
        """
        采用前序遍历
        :param node: Node
        :param depth: Int 深度
        :return:
        """
        if node == None:
            return
        # 创建深度层次
        if depth not in self.depth_dict.keys():
            self.depth_dict[depth] = list()
        # 处理在同一深度的节点
        else:
            # 带记忆的处理方式，将链尾的值指向下一个同深度的节点
            self.depth_dict[depth][-1].next = node
        self.depth_dict[depth].append(node) # 将结点存进去
        self.bfs(node.left,depth+1)
        self.bfs(node.right,depth+1)

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        核心思想:
            和前面一题的代码一毛一样

            类似DFS的感觉，将节点分层，一层的都添加到一个队列中。
            可以考虑设置深度，将一个深度的放在同一个列表中，构建深度字典
        """
        depth_dict = dict() # 深度词典初始化
        self.bfs(root,0)
        return root

