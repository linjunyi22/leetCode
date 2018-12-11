"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
1.The given integer is guaranteed to fit within the range of a 32-bit signed integer.
2.You could assume no leading zero bit in the integer’s binary representation.

给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。

注意:
给定的整数保证在32位带符号整数的范围内。
你可以假定二进制数不包含前导零位。

示例 1:
输入: 5
输出: 2
解释: 5的二进制表示为101（没有前导零位），其补数为010。所以你需要输出2。

示例 2:
输入: 1
输出: 0
解释: 1的二进制表示为1（没有前导零位），其补数为0。所以你需要输出0。
"""


class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        bin_l = list(bin(num)[2:])
        for i,v in enumerate(bin_l):
            if v == '0':
                bin_l[i] = '1'
            else:
                bin_l[i] = '0'

        return int(''.join(bin_l),2)

test = Solution().findComplement(5)
print(test)
