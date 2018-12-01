"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.

给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:
输入: 3
输出: [1,3,3,1]
"""


class Solution:
    def getRow(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return [1]
        elif numRows == 1:
            return [1,1]
        else:
            numRows += 1
            tmp_latest = [1,1]
            for _ in range(numRows - 2):
                tmp_gen = []
                for j in range(len(tmp_latest) - 1):
                    tmp_gen.append(tmp_latest[j] + tmp_latest[j+1])
                tmp_gen.append(1)
                tmp_latest = [1] + tmp_gen

            return tmp_latest

test = Solution().getRow(10)
print(test)
