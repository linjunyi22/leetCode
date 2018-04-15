"""
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.
写一个算法来判断一个数是不是“快乐数”。
一个数是不是快乐是这么定义的：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，或是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n != 1 and n != 4: # 无限循环时会出现4这个数字，当 n = 1时就是快乐数，n = 4直接跳出循环返回非快乐数
        	total = 0
        	n = str(n)
        	for i in n:
        		total += int(i)**2
        	n = total

        if n == 1:
        	return True 
        return False 

print(Solution().isHappy(19))
print(Solution().isHappy(123))