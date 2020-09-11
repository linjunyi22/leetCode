# 216. 组合总和 III
"""
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        combination = []
        range_list = range(1, 10)
        check_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]

        # 回溯
        def backtrack(k, n, index):
            if len(combination) == k and n == 0:
                ans.append(combination[:])
                return
            for i in range(index, 9):
                x = range_list[i]
                if n - x < 0:
                    return
                combination.append(x)
                # 每次递归要把上一层的数剔除掉，因为每个数字只能用一次
                backtrack(k, n-x, i+1)
                combination.pop(-1)

        # 最多包含 1-9，所以 k 大于 9 的话，直接返回空值
        if k > 9:
            return []
        # 最多 9 个数，从最大的数开始数，数到第 k 个，加起来的数比 n 还小的话，那就没有符合的组合，也直接返回空值
        if sum(check_list[:k]) < n:
            return []
        backtrack(k, n, 0)
        return ans
