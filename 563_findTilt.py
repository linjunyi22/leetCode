"""
Given a binary tree, return the tilt of the whole tree.
The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.
The tilt of the whole tree is defined as the sum of all nodes' tilt.

给定一个二叉树，计算整个树的坡度。
一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。
整个树的坡度就是其所有节点的坡度之和。


示例:
输入: 
         1
       /   \
      2     3
输出: 1
解释: 
结点的坡度 2 : 0
结点的坡度 3 : 0
结点的坡度 1 : |2-3| = 1
树的坡度 : 0 + 0 + 1 = 1

注意:
1.任何子树的结点的和不会超过32位整数的范围。
2.坡度的值不会超过32位整数的范围。

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum_,tilt_ = self._tiltsum(root)
        return tilt_
    
    def _tiltsum(self, node):
        if not node:
            return 0,0

        # 后序遍历用于获取左右子树的和
        sum_left, tilt_left = self._tiltsum(node.left)
        sum_right, tilt_right = self._tiltsum(node.right)

        # 单个节点的 tilt 是左右子树和的差的绝对值，需要将所有 tilt 加起来
        tilt_ = abs(sum_left - sum_right) + tilt_left + tilt_right 
        # 左右子树的和
        sum_ = sum_left + sum_right + node.val
        return sum_,tilt_

if __name__ == '__main__':
	test = Solution().findTilt([1,2,3,4,5,6,7])
	print(test)
