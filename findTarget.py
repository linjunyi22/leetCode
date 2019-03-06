"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

案例 1:

输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

输出: True
 

案例 2:

输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

输出: False

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return False
        
        # 设定一个集合，其中存放 k 与节点的差值
        # 层次遍历，每次遍历先判断值在不在集合中，如果在，返回 True，如果不在，把k 与节点的差值放进集合，以此类推
        s = set()
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.val in s:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            s.add(k - node.val)
        return False
                
if __name__ == '__main__':
	test = Solution().findTarget([1,2,3],4)
	print(test)
