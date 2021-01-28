# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        if head.next == None:
            return head

        res = ListNode(None)
        res = head

        while True:
            if head == None:
                break
            if head.next == None:
                break
            temp = head.val
            nextNode = head.next
            head.val = nextNode.val
            nextNode.val = temp
            head = head.next.next
        return res