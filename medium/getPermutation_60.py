# 60. 第k个排列
"""
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 每次计算只取当前能够能够排的最大的值，之后取出一个，然后递归处理
class Solution:
    def helper(self, n):
        if n <= 2:
            return n
        return n * self.helper(n - 1)

    def dfs(self, n, k, l):
        if n == 1:
            return str(l[0])
        # n 个数，按顺序排，每增加一个数则增加 count 次
        count = self.helper(n) // n
        s = ''
        tmp = 0
        for (i, v) in enumerate(l):
            tmp += count
            if tmp >= k:
                l.remove(v)
                s += str(v)
                k -= tmp - count
                break
        return s + self.dfs(n - 1, k, l.copy())

    def getPermutation(self, n: int, k: int) -> str:
        l = list(range(1, n+1))
        return self.dfs(n, k, l.copy())
