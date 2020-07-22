"""
给定一个二叉树，在树的最后一行找到最左边的值。

示例 1:

输入:

    2
   / \
  1   3

输出:
1
 

示例 2:

输入:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

输出:
7
 
注意: 您可以假设树（即给定的根节点）不为 NULL。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-bottom-left-tree-value
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 深度搜索，记录每个深度下的数据，最大深度的第一个元素即为最左元素
class Solution:
    def __init__(self):
        self.d = {}

    def findBottomLeftValue(self, root: TreeNode) -> int:
        def dfs(node, depth):
            if not node:
                return
            if depth in self.d:
                self.d[depth].append(node.val)
            else:
                self.d[depth] = [node.val]
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 1)
        max_depth = max(self.d)
        return self.d[max_depth][0]

# 广度搜索
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 本解法源于该题下的题解，详情请查阅链接内容
# 作者：quantbruce
# 链接：https://leetcode-cn.com/problems/find-bottom-left-tree-value/solution/bfsgai-jin-fa-jian-dan-yi-dong-jie-jin-shuang-bai-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.right:  # 先右后左
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val
