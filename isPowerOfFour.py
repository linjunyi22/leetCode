"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。

示例 1:
输入: 16
输出: true

示例 2:
输入: 5
输出: false

"""


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num>0:
            if num%4==0:
                num/=4
            else: 
                break
        return True if num==1 else False

test = Solution().isPowerOfFour(16)
print(test)
