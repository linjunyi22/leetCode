"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

不使用运算符 + 和-，计算两整数a 、b之和。

示例：
若 a = 1 ，b = 2，返回 3。

"""


class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return sum([a,b])

test = Solution().getSum(1,2)
print(test)
