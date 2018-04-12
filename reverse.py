"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
给定一个范围为 32 位 int 的整数，将其颠倒
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = ''
        if x >= 0:
        	x_list = list(str(x))
        	for i in reversed(x_list):
        		result += i
        	result = int(result)
        	if result > 2**32 - 1:
        		return 0
        	else:
        		return result
        else:
        	x_list = list(str(x))[1:]
        	for i in reversed(x_list):
        		result += i
        	result = '-' + result
        	result = int(result)
        	if result < -2**32 - 1:
        		return 0
        	else:
        		return result
        
print(Solution().reverse(123456789))