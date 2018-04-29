"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:
输入: x = 1, y = 4
输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。
"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x < 0 or y < 0 or x > 2**31 or y > 2**31:
        	return '输入错误'

        # 十进制转二进制
        x = bin(x)[2:]
        y = bin(y)[2:]

        # 短的前面补零
        if len(x) > len(y):
        	zero = "{}".format('0'*(len(x)-len(y)))
        	y = zero + y
        elif len(x) < len(y):
        	zero = "{}".format('0'*(len(y)-len(x)))
        	x = zero + x
        else:
        	pass

        # 比较不同
        count = 0 
        for i in zip(list(x),list(y)):
        	if i[0] != i[1]:
        		count += 1

        return count

test = Solution().hammingDistance(1,4)
print(test)
