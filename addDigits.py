"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:
Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.


给一个非负整数 num，反复添加所有的数字，直到结果只有一个数字。

例如:
设定 num = 38，过程就像： 3 + 8 = 11, 1 + 1 = 2。 由于 2 只有1个数字，所以返回它。
"""

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        from functools import reduce
        while num > 9:
            num = reduce(lambda x,y:x+y,map(int,list(str(num))))
        return num

test = Solution().addDigits(2328374)
print(test)