"""
Given a binary tree, return the inorder traversal of its nodes' values.

给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = []
        
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self._handler(root)
        return self.res

    def _handler(self, node):
        if node is None:
            return None
        self._handler(node.left)
        self.res.append(node.val)
        self._handler(node.right)
