# 40. 组合总和 II
"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []

        def backtrack(candidates, target, index):
            if target == 0:
                ans.append(path[:])
                return
            for i in range(index, len(candidates)):
                x = candidates[i]
                # 此处 if 判断是为了做去重处理，前提是数组已升序排序
                # 举例：arr = [1,2,2,3,4,5]，target = 7
                # 假设第一个 2 和 5已经组合成一个结果，那么连续两个 2 排列，后面的 2 肯定是重复的，所以要跳过不再判断
                # 因此 i > index 是要确定判断的是 index 后面的数（因为 index 已经在上一轮递归中判断了
                # 其次 candidates[i] == candidates[i - 1] 就能够找到连续且相同的数字
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                if target - x < 0:
                    return
                path.append(x)
                backtrack(candidates, target - x, i + 1)
                path.pop(-1)
            return

        candidates.sort()
        backtrack(candidates, target, 0)
        return ans
