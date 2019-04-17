"""
Write a program to find the node at which the intersection of two singly linked lists begins.

编写一个程序，找到两个单链表相交的起始节点。

注意：

如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        res = set()
        while headA or headB:
            if headA:
                if headA not in res:
                    res.add(headA)
                else:
                    return headA
                headA = headA.next
            if headB:
                if headB not in res:
                    res.add(headB)
                else:
                    return headB
                headB = headB.next
        return None
        