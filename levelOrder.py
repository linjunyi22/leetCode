"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
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
        return res

if __name__ == '__main__':
	test = Solution().levelOrder([3,9,20,None,None,15,7])
	print(test)

