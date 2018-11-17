"""
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。

示例1:
输入: 5
输出: True
解释: 1 * 1 + 2 * 2 = 5

示例2:
输入: 3
输出: False
"""


class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if int(c**0.5) == c**0.5:
            return True
        else :
            heigh = int(c**0.5)
        low = 1
        while  low <= heigh:
            if low**2 + heigh**2 > c:
                heigh -= 1
            elif low**2 + heigh**2 <c:
                low += 1
            else :
                return True
        return False

test = Solution().judgeSquareSum(5)
print(test)
