"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 与102.二叉树的层次遍历一样，但返回的是倒序结果，同样采用广度优先搜索遍历，最后对数组进行倒序排列即可

        if not root:
            return []
        
        res = []
        queue = [root]
        
        # 使用BFS 广度优先搜索
        while queue:
            level_size = len(queue) # 用于记录本层的所有节点数
            current_level = [] # 记录本层节点的值
            
            # 将本层所有节点遍历一次
            for i in range(level_size):
                node = queue.pop(0)
                current_level.append(node.val) 

                # 每次遍历将下一层的所有节点都添加到队列中
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(current_level)
        res.reverse() # 数组倒序
        return res

if __name__ == '__main__':
    test = Solution().levelOrder([3,9,20,None,None,15,7])
    print(test)
