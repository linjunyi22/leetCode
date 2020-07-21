"""
给你一棵二叉树，请你返回层数最深的叶子节点的和。

示例：
输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
输出：15

提示：

树中节点数目在 1 到 10^4 之间。
每个节点的值在 1 到 100 之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/deepest-leaves-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.res = {}

    def deepestLeavesSum(self, root: TreeNode) -> int:
        def helper(node, depth):
            if not node:
                return
            if node and node.left is None and node.right is None:
                if depth not in self.res:
                    self.res[depth] = [node.val]
                else:
                    self.res[depth].append(node.val)
                return
            helper(node.left, depth + 1)
            helper(node.right, depth + 1)
        helper(root, 1)
        max_depth = max(self.res)
        return sum(self.res[max_depth])
