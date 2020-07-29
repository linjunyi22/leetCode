"""
给定一个 N 叉树，返回其节点值的后序遍历。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.res = []

        def dfs(root):
            if not root:
                return
            for i in root.children:
                dfs(i)
                self.res.append(i.val)
        dfs(root)
        if root:
            self.res.append(root.val)
        return self.res
