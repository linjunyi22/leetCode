"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.

假设你正在爬楼梯。需要 n 步你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 步 + 1 步
2.  2 步

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 步 + 1 步 + 1 步
2.  1 步 + 2 步
3.  2 步 + 1 步

"""

"""
一开始做这道题的时候想到的是排列组合，但发现如果楼梯数（n）比较大的时候，排列组合貌似就很难了。。
于是在网上找了下有没有其他解决方法，于是发现动态规划的题目有很多解答方法都那么让人惊叹。

这道题可以使用斐波那契数列的思想：
设S(n)表示走n级台阶的走法数量。
走n级台阶，第一步只有两种选择：可以选择走1阶，然后还有S(n-1)种走法；
选择走2阶，那么接下来有S(n-2)种走法。那么S(n) = S(n-1) + S(n-2)。

"""
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 1
        for i in range(n):
            a, b = b, a + b
        return a    


test = Solution().climbStairs(6)
print(test)





