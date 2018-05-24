"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：
num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库，也不能直接将输入的字符串转换为整数形式。

"""

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = eval(num1)
        num2 = eval(num2)
        result = '{}'.format(num1 + num2)
        return result

test = Solution().addStrings('123', '456')
print(test)
