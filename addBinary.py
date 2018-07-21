"""
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

给定两个二进制字符串，返回他们的和（用二进制表示）。
输入为非空字符串且只包含数字 1 和 0。

示例 1:
输入: a = "11", b = "1"
输出: "100"

示例 2:
输入: a = "1010", b = "1011"
输出: "10101"
"""
class Solution(object):		
	def addBinary(self, a, b):
		a = int(a,2)
		b = int(b,2)
		tmp = a + b
		tmp = bin(tmp)
		result = tmp[2:]
		return result

test = Solution().addBinary('0','0')
print(test)
