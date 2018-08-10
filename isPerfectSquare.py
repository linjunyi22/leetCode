"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Note: Do not use any built-in library function such as sqrt.

给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

注意：不要使用任何内置的库函数，如  sqrt。

示例 1：
输入： 16
输出： True
 
示例 2：
输入： 14
输出： False
"""


class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        count = 1
        while True:
        	num -= count
        	if num == 0:
        		return True
        	elif num < 0:
        		return False
        	count += 2

test = Solution().isPerfectSquare(121)
print(test)
