# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def timeout(self, headA, headB):
        """
        考虑用list分别分出两个head出现的节点, 然后遍历就好了 直到有首个重复的节点结束
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        listA = [] # 专门存储A的节点
        listB = [] # 专门存储B的节点
        while headA != None or headB != None:
            listA.append(headA)
            listB.append(headB)
            if headB in listA:
                return headB
            if headA in listB:
                return headA
            if headA != None:
                headA = headA.next
            if headB != None:
                headB = headB.next
        return None
    def getIntersectionNode(self, headA, headB):
        """
        参考了一下大佬的思路，由于两个链表长度不相同，但是可以使用另外一种办法让他们的长度变得一样长
        让两个head同时出发，如果其中一个head走到头了，则开始走另一个head的路，这样两条路长度就一样了，就会在同一个点相同，有点类似莫比乌斯环的感觉后面给图示
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        # 开始走
        h1 = headA
        h2 = headB
        flag1 = True
        flag2 = True
        while h1 != h2:
            if h1 is not None:
                if h1.next is not None:
                    h1 = h1.next
                else:
                    if flag1:
                        h1 = headB
                        flag1 = False
                    else:
                        h1 = None
            if h2 is not None:
                if h2.next is not None:
                    h2 = h2.next
                else:
                    if flag2:
                        h2 = headA
                        flag2 = False
                    else:
                        h2 = None
        return h1
