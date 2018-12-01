"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            result = [[1],[1,1]]
            tmp_latest = [1,1]  #最新的行，用于生成下一行
            for _ in range(numRows - 2):
                tmp_gen = []  #存放生成的新行
                for j in range(len(tmp_latest) - 1):
                    tmp_gen.append(tmp_latest[j] + tmp_latest[j+1])
                tmp_gen.append(1)
                tmp_latest = [1] + tmp_gen
                result.append(tmp_latest)
            return result

test = Solution().generate(10)
print(test)
