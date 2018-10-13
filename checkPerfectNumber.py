"""
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.

对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。
给定一个 正整数 n， 如果他是完美数，返回 True，否则返回 False

示例：
输入: 28
输出: True
解释: 28 = 1 + 2 + 4 + 7 + 14

注意:
输入的数字 n 不会超过 100,000,000. (1e8)
"""


class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ans = 1
        if num%2 != 0:
            return False
        for i in range(1, num):
            if num%(2**i) == 0:
                ans += 2**i
                if ans == num/(2**i):
                    return True
            if num < 2**i:
                return False
        return False

test = Solution().checkPerfectNumber(6)
print(test)
