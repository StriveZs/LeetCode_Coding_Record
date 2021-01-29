# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(val=0)
        current = head
        prev = dummy
        next = ListNode(val=0)
        dummy.next = head
        length = 0
        # 计算长度
        while head != None:
            length += 1
            head = head.next
        head = dummy.next  # 恢复head
        if length < k:
            return head
        part = int(length / k)  # 共有多少个整数组
        yushu = length % k # 余数
        for i in range(part):
            for j in range(k-1):
                next = current.next
                current.next = next.next
                next.next = prev.next
                prev.next = next
            prev = current
            current = prev.next

        return dummy.next

if __name__ == '__main__':
    ln1 = ListNode(val=1)
    ln2 = ListNode(val=2)

    ln1.next = ln2

    s = Solution()
    print(s.reverseKGroup(ln1,2).val)