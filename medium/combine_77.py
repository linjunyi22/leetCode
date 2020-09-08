# 77. 组合
"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combinations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 回溯 
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start):
            if len(path) == k:
                res.append(path.copy())
            else:
                for i in range(start, n+1):
                    path.append(i)
                    backtrack(i + 1)
                    path.pop(-1)
        backtrack(1)
        return res
