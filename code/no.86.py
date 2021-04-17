class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode

        核心思想：大于x的第一个节点后面小于x的节点全部放到第一个节点前面(保持节点间的相对位置不变，不需要排序)
                1.小于 x 部分的链表按照原始顺序 记为 p
                2.大于等于 x 部分的链表按照原始顺序 记为 q
                3.拼接两个链表，p --> q
        """
        a = left = ListNode()
        b = right = ListNode()
        while head != None:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        left.next = b.next # 拼接
        right.next = None
        return a.next