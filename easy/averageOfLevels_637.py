"""
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

示例 1：

输入：
    3
   / \
  9  20
    /  \
   15   7
输出：[3, 14.5, 11]

解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
 
提示：
节点值的范围在32位有符号整数范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/average-of-levels-in-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        queue = [root]
        layList = []
        res = [root.val]
        while len(queue) > 0:
            r = queue.pop(0)
            if r.left:
                layList.append(r.left)
            if r.right:
                layList.append(r.right)
            if len(queue) == 0:
                queue = layList.copy()
                if len(layList) > 0:
                    res.append(sum([i.val for i in layList])/len(layList))
                layList = []
        return res
