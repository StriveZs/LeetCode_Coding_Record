# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    return_node = None
    flag = True
    def detectCycle(self, head):
        """
        dfs遍历，返回环的第一个节点就好了
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None
        self.return_node = None
        self.flag = True # 结束标志
        meomory = [] # 记忆列表

        def dfs(node):
            if self.flag:
                if node is not None:
                    if node in meomory:
                        self.return_node = node
                        self.flag = False
                    meomory.append(node)
                    dfs(node.next)

        dfs(head)
        return self.return_node