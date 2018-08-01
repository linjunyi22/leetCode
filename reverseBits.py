"""
Reverse bits of a given 32 bits unsigned integer.

颠倒给定的 32 位无符号整数的二进制位。

示例:
输入: 43261596
输出: 964176192

解释: 43261596 的二进制表示形式为 00000010100101000001111010011100 ，
     返回 964176192，其二进制表示形式为 00111001011110000010100101000000 。

进阶:
如果多次调用这个函数，你将如何优化你的算法？
"""


class Solution(object):
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
    	bin_n = list(bin(n))
    	bin_n_reversed = ''.join(reversed(bin_n[2:]))
    	bin_n_reversed += (32 - len(bin_n_reversed))*'0'
    	result = int(bin_n_reversed,2)
    	return result

test = Solution().reverseBits(43261596)
print(test)



