# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insertionSortList(self, head):
        """
        插入排序：除了第一个节点不动，第二个元素和前面已经排序好的元素进行比较，插入到合适的位置
        重复上述过程即可。
        比如:
            1 3 5 2 4   |左边为排序好的节点
            1 | 3 5 2 4
            1 3 | 5 2 4
            1 3 5 | 2 4
            1 2 3 5 | 4
            1 2 3 4 5 |
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next is None:
            return head
        ends = head.next
        node = head.next
        start = head
        # 单独处理前两个节点
        if node.val < start.val:
            start.next = node.next
            node.next = start
            ends = start
            start = node
            head = node
        # 递归处理后面所有情况
        node = ends.next
        while node is not None:
            # 寻找合适的插入位置 (3种情况：头插入、中间插入、尾插入)
            # 头插入
            if node.val < start.val:
                ends.next = node.next
                node.next = start
                start = node
                head = node
                node = ends.next
            # 尾插入
            elif node.val > ends.val:
                ends = node
                node = ends.next
            # 中间插入
            else:
                cur = start
                # 寻找插入位置
                while True:
                    if node.val >= cur.val and node.val <=cur.next.val:
                        break
                    cur = cur.next
                # 插入
                ends.next = node.next
                node.next = cur.next
                cur.next = node
                node = ends.next
        return head