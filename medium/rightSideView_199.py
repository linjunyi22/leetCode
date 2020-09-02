# 199. 二叉树的右视图
"""
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-right-side-view
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 按照题意，实际上就是取每一层的最右的节点
# 层次迭代遍历后取每层最右节点的值即可
# 每个节点遍历一次，时间复杂度 O(n)，空间复杂度 O(n)
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        row = list()
        res = [root.val]
        while len(queue) != 0:
            node = queue.pop(0)
            if node.left:
                row.append(node.left)
            if node.right:
                row.append(node.right)
            # queue 为零则代表当前该层遍历完成，获取 row 存储的下一层节点继续遍历
            if len(queue) == 0:
                queue = row.copy()
                if len(row) > 0 and row[-1]:
                    res.append(row[-1].val)
                row = list()
        return res


# 递归遍历
# 记录每层的值，最后遍历获取最右值即可
# 时间复杂度 O(n)，空间复杂度 O(n)
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.queue = []

        def dfs(root, depth):
            if not root:
                return
            if len(self.queue) <= depth:
                self.queue.append([])
            self.queue[depth].append(root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 0)
        return [i[-1] for i in self.queue]
