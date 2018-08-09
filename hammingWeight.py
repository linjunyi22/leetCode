"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。

示例 :
输入: 11
输出: 3
解释: 整数 11 的二进制表示为 00000000000000000000000000001011
 

示例 2:
输入: 128
输出: 1
解释: 整数 128 的二进制表示为 00000000000000000000000010000000

"""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bin_num = bin(n)
        result = bin_num.count('1')
        return result

test = Solution().hammingWeight(11)
print(test)
