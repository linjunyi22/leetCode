"""
Reverse a singly linked list.
click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?

反转一个单链表。

进阶:
链表可以迭代或递归地反转。你能否两个都实现一遍？
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 迭代方法反转
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None: # 表头是None或头指针，直接返回表头
        	return head

        cur = head # 当前节点变量
        newhead = None # 新的表头变量
        tmp = None # 临时变量，存储当前节点的下一个节点

        while cur:
        	tmp = cur.next # 当前节点的下一个节点
        	cur.next = newhead # 当前节点的下一个节点指向新表头，即把指针反转
        	newhead = cur # 更新当前节点作为新表头
        	cur = tmp # 更新当前节点为下一个节点，继续迭代

        return newhead

p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p1.next = p2
p2.next = p3
p3.next = None

test =  Solution().reverseList(p1)
print(test)

while test:
	print(test.val)
	test = test.next
