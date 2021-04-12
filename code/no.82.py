# Definition for singly-linked list.

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        核心思想：
                顺序访问链表，每次访问的元素如果不在stack中，则将该元素添加进去
                后面如果访问的元素在栈中，则删除这个结点
        """
        if head == None:
            return head
        # 单独处理只有一个结点的情况
        if head.next == None:
            return head
        listNode = []
        listNode.append(head.val)
        deleteList = [] # 删除节点集合
        temp = head.next
        pre = head # 记录前一个结点, 方便执行删除操作
        # 这个循环处理不了要删除的第一个结点
        while temp != None: # 这个约束保证了最少有两个结点，对于一个结点直接返回就好了
            if temp.val in listNode:
                pre.next = temp.next # 删除中间的结点
                deleteList.append(temp.val)
            else:
                listNode.append(temp.val) # 如果不在listNode中则添加进入
                pre = temp # 前指针向后移动一个
            temp = temp.next  # 指针指向下一个节点
        tt = head.next
        t_pre = head
        # 再处理要删除的第一个节点
        while tt != None:
            if tt.val in deleteList:
                t_pre.next = tt.next  # 删除中间的结点
            else:
                t_pre = tt
            tt = tt.next
        if head.val in deleteList:
            head = head.next
        return head
if __name__ == '__main__':
    s = Solution()
    a1 = ListNode(val=1)
    a2 = ListNode(val=3)
    a3 = ListNode(val=3)
    #a4 = ListNode(val=3)
    #a5 = ListNode(val=4)
    #a6 = ListNode(val=4)
    #a7 = ListNode(val=5)
    a1.next = a2
    a2.next = a3
    #a3.next = a4
    #a4.next = a5
    #a5.next = a6
    #a6.next = a7
    heads=s.deleteDuplicates(a1)
    while heads != None:
        print(heads.val)
        heads = heads.next