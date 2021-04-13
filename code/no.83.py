# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        核心思想：
                这道题排在上一道题后面我是没想到的
                直接拿上一道题的来改就好了
                就是上一道题的第一部分
        """
        temp = head
        while temp != None and temp.next != None:
            if temp.val == temp.next.val: # 重复元素
                temp.next = temp.next.next # 删除
            else:
                temp = temp.next
        return head