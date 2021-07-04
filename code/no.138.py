class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        题目分析：
            实质上就是链表的深度copy，同时要保留链表之间的random连接关系

            比较困难的一点就是: 如何找到random对应的节点关系

            想法：
                因为random_index是对应的节点索引，因此考虑先不设置random关系来构建一个完全相同的链表，并将节点对应的索引构建一个MAP和索引对应的节点构建一个MAP
                然后根据原来链表的random_index来构建索引关系
            构建：
                1. 旧链表：节点到index的映射
                2. 新链表：index到节点的映射
            第一遍遍历先构建一个全新的链表
            第二遍遍历在根据哈希关系构建random关系
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        index_node_dict = dict() # 新链表的index和节点对应关系
        node_index_dict = dict() # 旧链表的节点和index对应关系
        start = head
        new_head = Node(head.val)
        new_start = new_head
        index_node_dict[0] = new_head
        node_index_dict[head] = 0
        # 构建一个新的链表
        num = 1
        while start.next != None:
            start = start.next
            node = Node(start.val)
            new_start.next = node
            new_start = node
            index_node_dict[num] = node
            node_index_dict[start] = num
            num += 1
        # 构建random关系
        start = head
        new_start = new_head
        while start != None:
            # 单独处理为NULL情况
            if start.random is None:
                new_start.random = None
            else:
                new_start.random = index_node_dict[node_index_dict[start.random]] # random是按照index索引的
            start = start.next
            new_start = new_start.next

        return new_head
