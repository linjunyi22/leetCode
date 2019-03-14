"""
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

给定一个所有节点为非负值的二叉搜索树，求树中任意两节点的差的绝对值的最小值。

示例 :

输入:

   1
    \
     3
    /
   2

输出:
1

解释:
最小绝对差为1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
注意: 树中至少有2个节点。

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 二叉搜索树中序遍历后的结果是升序排列的，因此比较两两相邻的数字的差的绝对值即可。

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.queue = []
        self._middleorder(root)

        # 先取前两个值的差的绝对值做初始化值
        res = abs(self.queue[1] - self.queue[0])
        for i in range(1,len(self.queue) - 1):
            res = min(res,abs(self.queue[i+1] - self.queue[i]))
        return res
        
    def _middleorder(self,node):
        if node:
            self._middleorder(node.left)
            self.queue.append(node.val)
            self._middleorder(node.right)

if __name__ == '__main__':
    test = Solution().getMinimumDifference([2,1,3])
    print(test)
