"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.


将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 一个为空则返回另一个，两个都为空，返回任意一个都可以
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        # 新表头，用于记录
        newhead = ListNode(0)
        curnode = newhead
        
        while(l1 or l2):
        	# 任意一个遍历完了，直接在表尾接上另一个
            if l1 is None:
                curnode.next = l2
                break
            if l2 is None:
                curnode.next = l1
                break
            
            # 比较大小，符合的就往新链表表尾插入
            if l1.val < l2.val:
                curnode.next = l1
                curnode = curnode.next
                l1 = l1.next
            else:
                curnode.next = l2
                curnode = curnode.next
                l2 = l2.next
        return newhead.next
