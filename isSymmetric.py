"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.recursion(root.left,root.right)
    
    # 辅助函数
    def recursion(self,l,r):
        if l and r:
        	# 递归判断左右节点本身的值是否相等，然后取镜像对应的点再重复判断，以此类推，若遇到不符合的值，则返回False，最终结果全部进行与运算。
            return l.val == r.val and self.recursion(l.left,r.right) and self.recursion(l.right,r.left)
        return not l and not r

if __name__ == '__main__':
	test = Solution().isSymmetric([1,2,2,3,4,4,3])
	print(test)
