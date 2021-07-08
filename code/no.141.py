# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    flag = True
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        if head.next is None:
            return False
        self.flag = True
        node_list = [] # 记忆node，如果出现过则表示存在环了
        def dfs(node):
            if node.next != None:
                if node in node_list:
                    self.flag = False
                    return
                node_list.append(node)
                dfs(node.next)
        dfs(head)
        if self.flag:
            return False
        else:
            return True

