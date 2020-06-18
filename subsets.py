"""
幂集。编写一种方法，返回某集合的所有子集。集合中不包含重复的元素。

说明：解集不能包含重复的子集。

示例:

输入： nums = [1,2,3]
输出：
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""


"""
该题题解源自 https://leetcode-cn.com/problems/power-set-lcci/solution/die-dai-sheng-cheng-by-korlis/，作者：korlis

设 p(n) 表示 n 个元素的所有子集，那么有
p(0) = {}
p(1) = {}, {n1}
p(2) = {}, {n1}, {n2}, {n1, n2}
p(3) = {}, {n1}, {n2}, {n1, n2}, {n3}, {n1, n3}, {n2, n3}, {n1, n2, n3}
注意到 p(3) = p(2) + (n3 和每个 p(2) 元素的组合)
依次类推，我们就可以得到 p(n) 的计算方案，实际上就是在上层集合上不断的累计。
"""


class Solution:
    def subsets(self, nums):
        res = [[]]
        for i in nums:
            tmp = []
            for j in res:
                tmp.append(j+[i])
            res += tmp
        return res


if __name__ == "__main__":
    res = Solution().subsets([1, 2, 3, 4])
    print(res)
