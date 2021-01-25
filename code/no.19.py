# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        """
            基本思想：由于是寻找从后往前数第n个，因此第一遍先正数n个，然后第二遍再从头开始往后遍历同时第一遍正数的从n开始为空之后，这样第二遍数的就变为到空还有n个
            然后在去掉第倒数n个节点就行了。
        """
        a = head
        b = head
        # 第一遍数n个
        for i in range(n):
            if a.next:
                a = a.next
            else:
                return head.next
        # 接着数第一遍的同时，第二遍从头开始
        while a.next:
            a = a.next
            b = b.next
        b.next = b.next.next
        return head

