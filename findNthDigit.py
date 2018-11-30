"""
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。

注意:
n 是正数且在32为整形范围内 ( n < 231)。

示例 1:
输入:
3

输出:
3

示例 2:
输入:
11

输出:
0

说明:
第11个数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是0，它是10的一部分。
"""


class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """

        digit = 1
        while n > digit * 9 * 10 ** (digit - 1):
            n -= digit * 9 * 10 ** (digit - 1)
            digit += 1

        m = int((n - 1) / digit)
        n = int((n - 1) % digit)
        num = 10 ** (digit - 1) + m
        res = list(str(num))[n:n+1]
        return int(res[0])

test = Solution().findNthDigit(100)
print(test)
