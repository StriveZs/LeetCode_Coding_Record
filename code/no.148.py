# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    # fixme: 归并排序(自底向上合并链表)
    def merge(self, node1, node2):
        dummy = ListNode()
        pre = dummy
        while node1 is not None and node2 is not None:
            if node1.val <= node2.val:
                pre.next = node1
                pre = pre.next
                node1 = node1.next
            else:
                pre.next = node2
                pre = pre.next
                node2 = node2.next
        if node1 is not None:
            pre.next = node1
        if node2 is not None:
            pre.next = node2
        return dummy.next

    # fixme: 归并排序(自顶向下划分链表)
    def merge_sort(self, head):
        if head is None or head.next is None:
            return head
        # 快慢指针寻找中间节点
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        # 找到中间节点之后断开链表
        new_head = slow.next
        slow.next = None
        # 递归断开所有的节点
        slow = self.merge_sort(head)
        fast  =self.merge_sort(new_head)

        # 合并
        return self.merge(slow, fast)

    def sortList(self, head):
        """
        参考大佬的题解考虑使用归并排序
        对于数组的归并排序来说，可以直接根据数组的长度来找到中间值，对于链表来说，我们可以通过快慢指针来找到中间节点
        然后采用递归的方法将链表层层断开，排序后
        最后再合并
        :type head: ListNode
        :rtype: ListNode
        """
        return self.merge_sort(head)