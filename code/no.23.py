# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # 合并两个列表
    def mergeTwoLists(self, l1, l2):
        res = ListNode(None)
        node = res
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        while l1 and l2:
            if l1.val < l2.val:
                node.next, l1 = l1, l1.next
            else:
                node.next, l2 = l2, l2.next
            node = node.next
        if l1:
            node.next = l1
        else:
            node.next = l2
        return res.next

    # 合并多个列表
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            res = None
            return res
        if len(lists) == 1:
            return lists[0]
        init = lists[0]
        for i in range(1,len(lists)):
            init = self.mergeTwoLists(init,lists[i])
        return init