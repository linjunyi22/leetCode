"""
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true

示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false

示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 深度搜索，前中后遍历都可以，把数据存起来再比较，但这个方法比较耗内存，O(n)的空间复杂度，而且递归了两次，其实这方法不是很好。
# 方法1
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        p_list,q_list = [],[]
        self._inorder(p,p_list)
        self._inorder(q,q_list)
        return p_list == q_list
    
    def _inorder(self,node,l):
        if node:
            l.append(node.val)
            self._inorder(node.left,l)
            self._inorder(node.right,l)
        else:
            l.append(None)

# 方法2
# 同样深度搜索，但这种方法不用开辟内存存储任何值，相对来说快很多。
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if q == None and p == None:
            return True
        
        elif p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        else:
            return False

if __name__ == '__main__':
	test = Solution().isSameTree(p,q)
	print(test)
