"""
Given an integer, write a function to determine if it is a power of three.

给定一个整数，写一个函数来判断它是否是 3 的幂次方。
"""

class Solution:
    def isPowerOfThree(self,n):
        """
        :type n: int
        :rtype: bool
        """
        while n>=3:
            if n != int(n):
                return False
            n = n/3

        if n == 1.0 or n==3.0:
            return True
        return False

test = Solution().isPowerOfThree(100)
print(test)
