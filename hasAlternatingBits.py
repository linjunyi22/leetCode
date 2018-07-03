"""
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

给定一个正整数，检查他是否为交替位二进制数：换句话说，就是他的二进制数相邻的两个位数永不相等。

示例 1:
输入: 5
输出: True
解释:
5的二进制数是: 101

示例 2:
输入: 7
输出: False
解释:
7的二进制数是: 111

示例 3:
输入: 11
输出: False
解释:
11的二进制数是: 1011

示例 4:
输入: 10
输出: True
解释:
10的二进制数是: 1010

"""

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n_bin = bin(n)
        tmp = list(n_bin.lstrip('0b'))
        for i in range(len(tmp)-1):
        	if tmp[i] == tmp[i+1]:
        		return False
        return True

test = Solution().hasAlternatingBits(5)
print(test)
