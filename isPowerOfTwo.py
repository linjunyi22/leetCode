"""
Given an integer, write a function to determine if it is a power of two.

给定一个整数，写一个函数来判断它是否是2的幂。
"""

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 2:
            if (int(list(str(n))[-1]) %2) == 1: # 2的幂次方个位数肯定是偶数，不符合的直接判定 False
                return False
            n = n//2 # 符合要求的肯定能整除，不能整除而 '//'又是向下取整，则返回奇数，那么上面的判断就可以直接判 False 了

        if n == 1 or n == 2: # 2的零次方和2的一次方
            return True
        return False

test0 = Solution().isPowerOfTwo(12351897)
test1 = Solution().isPowerOfTwo(2048)
test2 = Solution().isPowerOfTwo(10)

print(test0,test1,test2,sep='\n')