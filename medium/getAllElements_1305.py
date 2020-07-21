"""
给你 root1 和 root2 这两棵二叉搜索树。
请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。.

示例 1：
输入：root1 = [2,1,4], root2 = [1,0,3]
输出：[0,1,1,2,3,4]

示例 2：
输入：root1 = [0,-10,10], root2 = [5,1,7,0,2]
输出：[-10,0,0,1,2,5,7,10]

示例 3：
输入：root1 = [], root2 = [5,1,7,0,2]
输出：[0,1,2,5,7]

示例 4：
输入：root1 = [0,-10,10], root2 = []
输出：[-10,0,10]

示例 5：
输入：root1 = [1,null,8], root2 = [8,1]
输出：[1,1,8,8]

提示：

每棵树最多有 5000 个节点。
每个节点的值在 [-10^5, 10^5] 之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/all-elements-in-two-binary-search-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 当时直接想的遍历两棵树然后放到一个数组中再做排序
# 官方题解中有更好的解法，利用二叉搜索树中序遍历后是顺序升序的特性
# 遍历两棵树，然后放到两个数组，再归并排序
class Solution:
    def __init__(self):
        self.res = []

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def helper(node):
            if not node:
                return
            self.res.append(node.val)
            helper(node.left)
            helper(node.right)
        helper(root1)
        helper(root2)
        self.res.sort()
        return self.res


# 以下为官方题解
# 链接：https: // leetcode-cn.com/problems/all-elements-in-two-binary-search-trees/solution/liang-ke-er-cha-sou-suo-shu-zhong-de-suo-you-yua-3/
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(node, v):
            if not node:
                return
            dfs(node.left, v)
            v.append(node.val)
            dfs(node.right, v)

        v1, v2 = list(), list()
        dfs(root1, v1)
        dfs(root2, v2)
        ans, i, j = list(), 0, 0
        while i < len(v1) or j < len(v2):
            if i < len(v1) and (j == len(v2) or v1[i] <= v2[j]):
                ans.append(v1[i])
                i += 1
            else:
                ans.append(v2[j])
                j += 1
        return ans
